"""
Background job management utilities for qsLAM PCR pipeline.

Handles background process execution with monitor threads that track completion
and update job status in the database. Replaces the streaming architecture
with non-blocking background job processing.
"""

import os
import signal
import subprocess
import threading
import time
from typing import Dict, List, Optional, Any, Callable
import database as db
from run_utils import RunWorkspace
from pipeline_constants import validate_step_name


def start_background_job(run_id: str, step_name: str, command: List[str],
                        cwd: str = None, env: Dict[str, str] = None) -> int:
    """
    Start a background job with monitor thread.

    Args:
        run_id: Run identifier
        step_name: Pipeline step name (must be from PIPELINE_STEPS)
        command: Command to execute as list of strings
        cwd: Working directory for command execution
        env: Environment variables for command

    Returns:
        job_id: Database job ID for tracking
    """
    # Validate step name
    if not validate_step_name(step_name):
        raise ValueError(f"Invalid step name: {step_name}")
    workspace = RunWorkspace(run_id)
    log_file = workspace.get_log_file(step_name)

    # Create job record in database
    job_id = db.create_job(run_id, step_name, log_file)

    try:
        # Ensure log directory exists
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Start background process with new process group
        with open(log_file, 'w') as log_handle:
            process = subprocess.Popen(
                command,
                cwd=cwd,
                env=env,
                stdout=log_handle,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                preexec_fn=os.setsid  # Create new process group
            )

        # Get process group ID for job control
        pgid = os.getpgid(process.pid)

        # Update job status to running
        db.start_job(job_id, pgid)

        # Update run status
        db.update_run(run_id, status='running', current_step=step_name)

        # Start monitor thread
        monitor_thread = threading.Thread(
            target=_monitor_job_completion,
            args=(job_id, run_id, process, log_file),
            daemon=True
        )
        monitor_thread.start()

        print(f"Started background job {job_id} for run {run_id}, step {step_name}")
        return job_id

    except Exception as e:
        # If we can't start the job, mark it as failed
        db.complete_job(job_id, success=False, error_message=str(e))
        db.update_run(run_id, status='failed', current_step=None)
        raise


def _monitor_job_completion(job_id: int, run_id: str, process: subprocess.Popen, log_file: str):
    """
    Monitor thread that tracks background process completion.

    This function runs in a separate thread and updates the database when
    the background process completes.
    """
    try:
        # Wait for process to complete
        return_code = process.wait()

        # Log completion
        with open(log_file, 'a') as log_handle:
            log_handle.write(f"\n[MONITOR] Process completed with return code: {return_code}\n")

        # Update job status based on return code
        success = (return_code == 0)
        error_message = None

        if not success:
            # Read tail of log file to capture actual error output
            try:
                with open(log_file, 'r') as f:
                    lines = f.readlines()
                    # Get last lines before the [MONITOR] marker, excluding monitor's own output
                    tail_lines = [l for l in lines[-20:] if not l.startswith('[MONITOR]')]
                    error_message = ''.join(tail_lines[-10:]).strip()
                    if not error_message:
                        error_message = f"Process exited with code {return_code}"
            except Exception:
                error_message = f"Process exited with code {return_code}"

        db.complete_job(job_id, success=success, error_message=error_message)

        # Update run status (clear current_step)
        if success:
            db.update_run(run_id, current_step=None)
            print(f"Job {job_id} completed successfully")
        else:
            db.update_run(run_id, status='failed', current_step=None)
            print(f"Job {job_id} failed with return code {return_code}")

    except Exception as e:
        # Handle monitor thread errors
        error_msg = f"Monitor thread error: {str(e)}"
        print(f"ERROR: {error_msg}")

        with open(log_file, 'a') as log_handle:
            log_handle.write(f"\n[MONITOR ERROR] {error_msg}\n")

        db.complete_job(job_id, success=False, error_message=error_msg)
        db.update_run(run_id, status='failed', current_step=None)


def kill_job_by_id(job_id: int) -> bool:
    """
    Kill a running job by its database ID.

    Args:
        job_id: Database job ID

    Returns:
        True if job was killed, False if not found or not running
    """
    job = db.get_job(job_id)
    if not job:
        return False

    if job['status'] != 'running' or not job['pgid']:
        return False

    try:
        # Kill entire process group
        os.killpg(job['pgid'], signal.SIGTERM)

        # Give processes a chance to terminate gracefully
        time.sleep(2)

        # Force kill if still running
        try:
            os.killpg(job['pgid'], signal.SIGKILL)
        except ProcessLookupError:
            pass  # Process group already terminated

        # Update job status
        db.kill_job(job_id)

        # Update run status
        db.update_run(job['run_id'], current_step=None)

        print(f"Killed job {job_id} (PGID: {job['pgid']})")
        return True

    except ProcessLookupError:
        # Process group doesn't exist (already terminated)
        db.kill_job(job_id)
        db.update_run(job['run_id'], current_step=None)
        return True

    except Exception as e:
        print(f"Error killing job {job_id}: {str(e)}")
        return False


def kill_run_jobs(run_id: str) -> int:
    """
    Kill all running jobs for a run.

    Args:
        run_id: Run identifier

    Returns:
        Number of jobs killed
    """
    jobs = db.get_jobs_for_run(run_id)
    killed_count = 0

    for job in jobs:
        if job['status'] == 'running':
            if kill_job_by_id(job['id']):
                killed_count += 1

    return killed_count


def get_job_logs(run_id: str, step_name: str) -> str:
    """
    Get log content for a specific step in a run.

    Args:
        run_id: Run identifier
        step_name: Pipeline step name

    Returns:
        Log file content as string
    """
    workspace = RunWorkspace(run_id)
    log_file = workspace.get_log_file(step_name)

    if not os.path.exists(log_file):
        return f"Log file not found: {log_file}"

    try:
        with open(log_file, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading log file: {str(e)}"


def get_job_status(run_id: str, step_name: str) -> Optional[Dict[str, Any]]:
    """
    Get status of the most recent job for a step.

    Args:
        run_id: Run identifier
        step_name: Pipeline step name

    Returns:
        Job status dictionary or None if not found
    """
    return db.get_latest_job_for_step(run_id, step_name)


def cleanup_old_logs(days_old: int = 30) -> int:
    """
    Clean up log files older than specified days.

    Args:
        days_old: Remove logs older than this many days

    Returns:
        Number of log files removed
    """
    import glob
    import time

    runs_dir = "runs"
    if not os.path.exists(runs_dir):
        return 0

    cutoff_time = time.time() - (days_old * 24 * 60 * 60)
    removed_count = 0

    # Find all log files in all runs
    log_pattern = os.path.join(runs_dir, "*", "logs", "*.log")

    for log_file in glob.glob(log_pattern):
        try:
            if os.path.getmtime(log_file) < cutoff_time:
                os.remove(log_file)
                removed_count += 1
        except Exception as e:
            print(f"Error removing log file {log_file}: {e}")

    return removed_count




# Utility functions for common pipeline operations

def run_command_sync(command: List[str], cwd: str = None, env: Dict[str, str] = None) -> tuple[bool, str]:
    """
    Run a command synchronously and return result.

    Args:
        command: Command to execute as list of strings
        cwd: Working directory for command execution
        env: Environment variables for command

    Returns:
        (success, output) tuple
    """
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            env=env,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout for sync operations
        )

        output = result.stdout
        if result.stderr:
            output += "\nSTDERR:\n" + result.stderr

        return (result.returncode == 0, output)

    except subprocess.TimeoutExpired:
        return (False, "Command timed out after 5 minutes")
    except Exception as e:
        return (False, f"Command execution error: {str(e)}")


def validate_command_exists(command_name: str) -> bool:
    """
    Check if a command exists in the system PATH.

    Args:
        command_name: Name of command to check

    Returns:
        True if command exists, False otherwise
    """
    try:
        result = subprocess.run(
            ['which', command_name],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except:
        return False


def get_system_dependencies() -> Dict[str, bool]:
    """
    Check availability of required system dependencies.

    Returns:
        Dictionary mapping command names to availability status
    """
    required_commands = [
        'fastqc',
        'cutadapt',
        'bwa-mem2',
        'samtools',
        'bedtools',
        'perl',
        'Rscript',
        'fastp'
    ]

    return {cmd: validate_command_exists(cmd) for cmd in required_commands}