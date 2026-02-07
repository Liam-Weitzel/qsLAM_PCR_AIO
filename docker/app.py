"""
qsLAM PCR Pipeline - Multi-run Backend API

Flask application implementing the new multi-run architecture with:
- SQLite database for state management
- Background job processing with monitor threads
- Isolated run workspaces with shared reference genomes
- Complete audit trail and job history

Replaces the old streaming architecture with proper REST API endpoints.
"""

from flask import Flask, request, jsonify, send_file
import os
import traceback
from typing import Dict, Any, Optional

# Import our modules
import database as db
import run_utils
import job_utils
from pipeline_constants import validate_step_name, validate_genome

app = Flask(__name__)

# Configure Flask
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 * 1024  # 10GB max upload

def init_app():
    """Initialize the Flask application."""
    try:
        # Initialize database and shared directories
        db.init_db()
        print("✅ Database initialized successfully")

        # Verify system dependencies
        deps = job_utils.get_system_dependencies()
        missing_deps = [cmd for cmd, available in deps.items() if not available]

        if missing_deps:
            print(f"⚠️  Warning: Missing system dependencies: {', '.join(missing_deps)}")
        else:
            print("✅ All system dependencies available")

        print("🚀 qsLAM PCR Pipeline server ready")

    except Exception as e:
        print(f"❌ Failed to initialize application: {str(e)}")
        raise


def handle_error(error: Exception, endpoint: str = "") -> tuple[Dict[str, Any], int]:
    """Centralized error handling for API endpoints."""
    error_msg = str(error)

    # Log the full traceback for debugging
    print(f"ERROR in {endpoint}: {error_msg}")
    print("Full traceback:")
    traceback.print_exc()

    # Return appropriate error response
    if "not found" in error_msg.lower():
        return {"error": error_msg, "endpoint": endpoint}, 404
    elif "invalid" in error_msg.lower() or "unsupported" in error_msg.lower():
        return {"error": error_msg, "endpoint": endpoint}, 400
    else:
        return {"error": error_msg, "endpoint": endpoint}, 500


@app.errorhandler(404)
def not_found(error):
    return {"error": "Endpoint not found"}, 404


@app.errorhandler(500)
def internal_error(error):
    return {"error": "Internal server error"}, 500


# ===============================
# BASIC INFO ENDPOINTS
# ===============================

@app.route('/', methods=['GET'])
def index():
    """Basic server info."""
    return {
        "name": "qsLAM PCR Pipeline API",
        "version": "2.0.0",
        "status": "running"
    }


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    try:
        # Check database connection
        stats = db.get_database_stats()

        # Check system dependencies
        deps = job_utils.get_system_dependencies()
        missing_deps = [cmd for cmd, available in deps.items() if not available]

        return {
            "status": "healthy",
            "database": "connected",
            "active_jobs": stats.get("active_jobs", 0),
            "total_runs": stats.get("total_runs", 0),
            "missing_dependencies": missing_deps
        }
    except Exception as e:
        return handle_error(e, "health")


# ===============================
# SYSTEM MANAGEMENT
# ===============================

@app.route('/system/status', methods=['GET'])
def system_status():
    """Get comprehensive system status."""
    try:
        # Database statistics
        db_stats = db.get_database_stats()

        # Disk usage
        disk_usage = run_utils.get_disk_usage()

        # System dependencies
        deps = job_utils.get_system_dependencies()

        return {
            "database": db_stats,
            "disk_usage": disk_usage,
            "dependencies": deps,
            "available_genomes": run_utils.list_available_genomes()
        }
    except Exception as e:
        return handle_error(e, "system/status")


@app.route('/system/info', methods=['GET'])
def system_info():
    """Get system information."""
    return {
        "name": "qsLAM PCR Server",
        "version": "2.0.0",
        "deployment_mode": "local",
        "supported_genomes": list(run_utils.SUPPORTED_GENOMES.keys()),
        "pipeline_steps": [
            "qc", "umi", "cutadapt", "fastp",
            "readlen", "read_mapping", "site_analysis"
        ]
    }


@app.route('/system/genomes', methods=['GET'])
def list_genomes():
    """List supported genomes for frontend dropdown."""
    from pipeline_constants import SUPPORTED_GENOMES
    return {"genomes": list(SUPPORTED_GENOMES.keys())}


# ===============================
# RUN MANAGEMENT
# ===============================

@app.route('/runs', methods=['POST'])
def create_run():
    """Create a new run with configuration and uploaded files."""
    try:
        # Get form data and files
        name = request.form.get('name')
        description = request.form.get('description', '')
        created_by = request.form.get('created_by', 'anonymous')

        if not name:
            return {"error": "Run name is required"}, 400

        # Get uploaded files
        if 'R1' not in request.files or 'R2' not in request.files:
            return {"error": "Both R1 and R2 files must be uploaded"}, 400

        r1_file = request.files['R1']
        r2_file = request.files['R2']

        if r1_file.filename == '' or r2_file.filename == '':
            return {"error": "Both R1 and R2 files must be selected"}, 400

        # Extract configuration from form fields
        config = {}

        # Cutadapt configuration
        for field in ['r1_seq', 'r2_seq', 'r1_error_rate', 'r2_error_rate',
                     'r1_trim_leading_trailing', 'r2_trim_leading_trailing',
                     'r1_anchored', 'r2_anchored', 'r1_min_overlap', 'r2_min_overlap',
                     'r1_pair_filter', 'r2_pair_filter', 'r1_minimum_length_of_read', 'r2_minimum_length_of_read']:
            value = request.form.get(field)
            if value is not None:
                # Convert types appropriately
                if 'error_rate' in field:
                    config[field] = float(value)
                elif 'anchored' in field:
                    config[field] = value.lower() in ('true', '1', 'yes')
                elif field in ['r1_trim_leading_trailing', 'r2_trim_leading_trailing',
                              'r1_min_overlap', 'r2_min_overlap', 'r1_minimum_length_of_read', 'r2_minimum_length_of_read']:
                    config[field] = int(value)
                else:
                    config[field] = value

        # Read mapping configuration - genome is required
        genome = request.form.get('genome')
        if not genome:
            return {"error": "genome is required"}, 400
        if not validate_genome(genome):
            from pipeline_constants import SUPPORTED_GENOMES
            supported = ", ".join(SUPPORTED_GENOMES.keys())
            return {"error": f"Unsupported genome: '{genome}'. Supported genomes: {supported}"}, 400
        config['genome'] = genome

        # Site analysis configuration
        for field in ['promoter_left', 'promoter_right', 'enhancer_left']:
            value = request.form.get(field)
            if value is not None:
                config[field] = int(value)

        # Create run in database
        run_id = db.create_run(name=name, created_by=created_by, description=description, **config)

        # Create run workspace
        workspace = run_utils.create_run_workspace(run_id)

        # Save uploaded files
        run_utils.save_uploaded_files(run_id, r1_file, r2_file)

        return {
            "run_id": run_id,
            "name": name,
            "status": "pending",
            "message": "Run created successfully with uploaded files"
        }, 201

    except Exception as e:
        return handle_error(e, "create_run")


@app.route('/runs', methods=['GET'])
def list_runs():
    """List all runs with optional filtering."""
    try:
        created_by = request.args.get('created_by')
        limit = request.args.get('limit', type=int)

        runs = db.list_runs(created_by=created_by, limit=limit)

        return {"runs": runs}

    except Exception as e:
        return handle_error(e, "list_runs")


@app.route('/runs/<run_id>', methods=['GET'])
def get_run(run_id: str):
    """Get detailed information about a specific run."""
    try:
        run_data = db.get_run(run_id)
        if not run_data:
            return {"error": f"Run not found: {run_id}"}, 404

        # Get job history
        jobs = db.get_jobs_for_run(run_id)

        # Add job history to response
        run_data['jobs'] = jobs

        return run_data

    except Exception as e:
        return handle_error(e, "get_run")


@app.route('/runs/<run_id>/status', methods=['GET'])
def get_run_status(run_id: str):
    """Get run status with step history."""
    try:
        status_data = db.get_run_status(run_id)
        if not status_data:
            return {"error": f"Run not found: {run_id}"}, 404

        return status_data

    except Exception as e:
        return handle_error(e, "get_run_status")


@app.route('/runs/<run_id>', methods=['DELETE'])
def delete_run(run_id: str):
    """Delete a run and its workspace."""
    try:
        # Check if run exists
        run_data = db.get_run(run_id)
        if not run_data:
            return {"error": f"Run not found: {run_id}"}, 404

        # Kill any running jobs for this run
        killed_jobs = job_utils.kill_run_jobs(run_id)

        # Delete from database
        success = db.delete_run(run_id)
        if not success:
            return {"error": "Failed to delete run from database"}, 500

        # Clean up workspace
        run_utils.cleanup_run_workspace(run_id)

        return {
            "message": f"Run {run_id} deleted successfully",
            "killed_jobs": killed_jobs
        }

    except Exception as e:
        return handle_error(e, "delete_run")


@app.route('/runs/<run_id>/export', methods=['GET'])
def export_run_config(run_id: str):
    """Export run configuration for import on another server."""
    try:
        run_data = db.get_run(run_id)
        if not run_data:
            return {"error": f"Run not found: {run_id}"}, 404

        # Export configuration (no data files)
        config_data = run_utils.export_run_config(run_id, run_data)

        return config_data

    except Exception as e:
        return handle_error(e, "export_run_config")


@app.route('/runs/import', methods=['POST'])
def import_run_config():
    """Import run configuration from another server."""
    try:
        config_data = request.get_json()
        if not config_data:
            return {"error": "Configuration data is required"}, 400

        # Import configuration
        new_run_id, run_config = run_utils.import_run_config(config_data)

        # Create run in database
        run_id = db.create_run(**run_config)

        # Create workspace
        run_utils.create_run_workspace(run_id)

        return {
            "run_id": run_id,
            "message": "Run configuration imported successfully",
            "note": "Data files must be uploaded separately"
        }, 201

    except Exception as e:
        return handle_error(e, "import_run_config")


# ===============================
# PIPELINE STEP ENDPOINTS
# ===============================

def start_pipeline_step(run_id: str, step_name: str, command_builder_func):
    """Generic function to start any pipeline step."""
    # Validate step name
    if not validate_step_name(step_name):
        return {"error": f"Invalid step name: {step_name}"}, 400

    # Check if run exists
    run_data = db.get_run(run_id)
    if not run_data:
        return {"error": f"Run not found: {run_id}"}, 404

    # Check if there's already a job running for this run
    running_jobs = db.get_running_jobs()
    for job in running_jobs:
        if job['run_id'] == run_id:
            return {"error": f"Run {run_id} already has a running job: {job['step_name']}"}, 409

    try:
        # Build the command using the provided function
        command = command_builder_func(run_id, run_data)

        # Start background job
        job_id = job_utils.start_background_job(run_id, step_name, command)

        return {
            "job_id": job_id,
            "status": "started",
            "message": f"Started {step_name} for run {run_id}"
        }

    except Exception as e:
        return handle_error(e, f"start_{step_name}")


@app.route('/runs/<run_id>/qc', methods=['POST'])
def start_qc(run_id: str):
    """Start FastQC quality control step."""
    # Get stage from query parameter
    stage = request.args.get('stage', 'before')
    if stage not in ('before', 'after'):
        return {"error": f"Invalid QC stage: '{stage}'. Must be 'before' or 'after'"}, 400

    def build_qc_command(run_id: str, run_data: dict):
        workspace = run_utils.RunWorkspace(run_id)

        if stage == 'before':
            r1, r2 = workspace.get_rawdata_files()
            outdir = workspace.get_fastqc_output_dir('before')
        else:
            r1, r2 = workspace.get_cutadapt_files()
            outdir = workspace.get_fastqc_output_dir('after')

        # Ensure both input files exist
        if not (os.path.exists(r1) and os.path.exists(r2)):
            raise ValueError(f"Input files not found for QC stage: {stage}")

        return [
            'bash', '-c',
            f'mkdir -p {outdir} && fastqc -o {outdir} {r1} {r2}'
        ]

    return start_pipeline_step(run_id, 'qc', build_qc_command)


@app.route('/runs/<run_id>/umi', methods=['POST'])
def start_umi(run_id: str):
    """Start UMI processing step."""
    def build_umi_command(run_id: str, run_data: dict):
        # UMI processing not yet implemented in original pipeline
        # Return placeholder command
        return ['echo', 'UMI processing not yet implemented']

    return start_pipeline_step(run_id, 'umi', build_umi_command)


@app.route('/runs/<run_id>/cutadapt', methods=['POST'])
def start_cutadapt(run_id: str):
    """Start adapter trimming with cutadapt."""
    def build_cutadapt_command(run_id: str, run_data: dict):
        workspace = run_utils.RunWorkspace(run_id)
        r1_input, r2_input = workspace.get_rawdata_files()
        cut_dir = workspace.get_path('cutPrimer')

        # Ensure input files exist
        if not (os.path.exists(r1_input) and os.path.exists(r2_input)):
            raise ValueError("Input FASTQ files not found")

        # Get cutadapt configuration from run data
        config = {
            'r1_seq': run_data.get('r1_seq'),
            'r2_seq': run_data.get('r2_seq'),
            'r1_error_rate': run_data.get('r1_error_rate', 0.3),
            'r2_error_rate': run_data.get('r2_error_rate', 0.1),
            'r1_trim_leading_trailing': run_data.get('r1_trim_leading_trailing', 0),
            'r2_trim_leading_trailing': run_data.get('r2_trim_leading_trailing', 0),
            'r1_anchored': run_data.get('r1_anchored', False),
            'r2_anchored': run_data.get('r2_anchored', False),
            'r1_min_overlap': run_data.get('r1_min_overlap', 5),
            'r2_min_overlap': run_data.get('r2_min_overlap', 10),
            'r1_pair_filter': run_data.get('r1_pair_filter', 'both'),
            'r2_pair_filter': run_data.get('r2_pair_filter', 'both'),
            'r1_minimum_length_of_read': run_data.get('r1_minimum_length_of_read', 30),
            'r2_minimum_length_of_read': run_data.get('r2_minimum_length_of_read', 30)
        }

        if not config['r1_seq'] or not config['r2_seq']:
            raise ValueError("Cutadapt sequences (r1_seq, r2_seq) are required")

        # Build cutadapt command (2-step process)
        tmp1 = os.path.join(cut_dir, "step1_R1.fastq.gz")
        tmp2 = os.path.join(cut_dir, "step1_R2.fastq.gz")
        out1 = os.path.join(cut_dir, "R1.fastq.gz")
        out2 = os.path.join(cut_dir, "R2.fastq.gz")

        # Create complex bash command that runs both cutadapt steps
        r1_anchor = '^' if config['r1_anchored'] else ''
        r2_anchor = '^' if config['r2_anchored'] else ''

        command = f'''
        mkdir -p {cut_dir} &&
        cutadapt \
            -e {config["r1_error_rate"]} \
            --cut {config["r1_trim_leading_trailing"]} \
            -g "{r1_anchor}{config["r1_seq"]};min_overlap={config["r1_min_overlap"]}" \
            --pair-filter {config["r1_pair_filter"]} \
            -m {config["r1_minimum_length_of_read"]} \
            -j {os.cpu_count()} \
            -o {tmp1} -p {tmp2} \
            {r1_input} {r2_input} &&
        cutadapt \
            -e {config["r2_error_rate"]} \
            --cut {config["r2_trim_leading_trailing"]} \
            -G "{r2_anchor}{config["r2_seq"]};min_overlap={config["r2_min_overlap"]}" \
            --pair-filter {config["r2_pair_filter"]} \
            -m {config["r2_minimum_length_of_read"]} \
            -j {os.cpu_count()} \
            -o {out1} -p {out2} \
            {tmp1} {tmp2} &&
        rm -f {tmp1} {tmp2}
        '''

        return ['bash', '-c', command.strip()]

    return start_pipeline_step(run_id, 'cutadapt', build_cutadapt_command)


@app.route('/runs/<run_id>/fastp', methods=['POST'])
def start_fastp(run_id: str):
    """Start fastp quality processing."""
    def build_fastp_command(run_id: str, run_data: dict):
        workspace = run_utils.RunWorkspace(run_id)
        r1_input, r2_input = workspace.get_rawdata_files()

        # Fastp outputs go to rawdata with .fastp suffix
        tmp_r1 = workspace.get_path("rawdata", "R1.fastp.fastq.gz")
        tmp_r2 = workspace.get_path("rawdata", "R2.fastp.fastq.gz")

        # Ensure input files exist
        if not (os.path.exists(r1_input) and os.path.exists(r2_input)):
            raise ValueError("Input FASTQ files not found")

        return [
            'fastp',
            '-i', r1_input,
            '-I', r2_input,
            '-o', tmp_r1,
            '-O', tmp_r2
        ]

    return start_pipeline_step(run_id, 'fastp', build_fastp_command)


@app.route('/runs/<run_id>/readlen', methods=['POST'])
def start_readlen(run_id: str):
    """Start read length analysis."""
    def build_readlen_command(run_id: str, run_data: dict):
        workspace = run_utils.RunWorkspace(run_id)
        r1, r2 = workspace.get_cutadapt_files()

        # Ensure trimmed files exist
        if not (os.path.exists(r1) and os.path.exists(r2)):
            raise ValueError("Cutadapt output files not found. Run cutadapt first.")

        output_pdf = workspace.get_path('readlen', 'readlen.pdf')
        return [
            'Rscript', 'readlen_analysis.R', r1, r2, output_pdf
        ]

    return start_pipeline_step(run_id, 'readlen', build_readlen_command)


@app.route('/runs/<run_id>/read_mapping', methods=['POST'])
def start_read_mapping(run_id: str):
    """Start BWA-MEM2 read mapping."""
    def build_read_mapping_command(run_id: str, run_data: dict):
        workspace = run_utils.RunWorkspace(run_id)
        r1, r2 = workspace.get_cutadapt_files()
        bwa_files = workspace.get_bwa_files()

        # Ensure trimmed files exist
        if not (os.path.exists(r1) and os.path.exists(r2)):
            raise ValueError("Cutadapt output files not found. Run cutadapt first.")

        # Get genome configuration
        genome = run_data.get('genome')
        if not genome:
            raise ValueError("Genome is required for read mapping")

        # Check if genome is available or needs downloading
        if not run_utils.has_bwa_mem2_index(genome):
            from pipeline_constants import SUPPORTED_GENOMES
            genome_tar_url = SUPPORTED_GENOMES[genome]["tar_url"]
            print(f"Genome {genome} not found, will download from {genome_tar_url}")

        # Get path to genome index
        genome_fa = run_utils.get_shared_reference_path(genome)

        # Build complex BWA-MEM2 + samtools pipeline
        command = f'''
        mkdir -p {workspace.get_path("bwa")} &&
        {{
            if [ ! -f "{genome_fa}.0123" ]; then
                echo "Downloading genome {genome}..."
                python3 -c "import run_utils; run_utils.download_genome_if_needed('{genome}')"
            fi
        }} &&
        bwa-mem2 mem -t {os.cpu_count()} {genome_fa} {r1} {r2} -o {bwa_files["sam"]} &&
        samtools view -hb {bwa_files["sam"]} --threads {os.cpu_count()} -o {bwa_files["bam"]} &&
        samtools sort {bwa_files["bam"]} --threads {os.cpu_count()} -o {bwa_files["sorted_bam"]} &&
        samtools index {bwa_files["sorted_bam"]} --threads {os.cpu_count()} &&
        samtools flagstat {bwa_files["sorted_bam"]} --threads {os.cpu_count()} > {bwa_files["stats"]}
        '''

        return ['bash', '-c', command.strip()]

    return start_pipeline_step(run_id, 'read_mapping', build_read_mapping_command)


@app.route('/runs/<run_id>/site_analysis', methods=['POST'])
def start_site_analysis(run_id: str):
    """Start cutting site analysis and peak detection."""
    def build_site_analysis_command(run_id: str, run_data: dict):
        workspace = run_utils.RunWorkspace(run_id)
        bwa_files = workspace.get_bwa_files()

        # Ensure BWA outputs exist (prerequisite validation for immediate 400 response)
        if not os.path.exists(bwa_files["sorted_bam"]):
            raise ValueError("BWA output files not found. Run read_mapping first.")

        # Get configuration
        genome = run_data.get('genome')
        promoter_left = run_data.get('promoter_left', 5000)
        promoter_right = run_data.get('promoter_right', 2000)
        enhancer_left = run_data.get('enhancer_left', 50000)

        if not genome:
            raise ValueError("Genome is required for site analysis")

        # Resolve absolute paths for script execution
        workspace_abs = os.path.abspath(workspace.base_path)
        script_dir = os.path.abspath(os.path.dirname(__file__) or '.')

        return [
            'bash', os.path.join(script_dir, 'site_analysis.sh'),
            workspace_abs,
            script_dir,
            genome,
            str(promoter_left),
            str(promoter_right),
            str(enhancer_left)
        ]

    return start_pipeline_step(run_id, 'site_analysis', build_site_analysis_command)


# ===============================
# PIPELINE STEP STATUS/LOGS
# ===============================

@app.route('/runs/<run_id>/<step_name>/status', methods=['GET'])
def get_step_status(run_id: str, step_name: str):
    """Get status of a specific pipeline step."""
    try:
        if not validate_step_name(step_name):
            return {"error": f"Invalid step name: {step_name}"}, 400

        job_status = job_utils.get_job_status(run_id, step_name)
        if not job_status:
            return {"error": f"No job found for step {step_name} in run {run_id}"}, 404

        return job_status

    except Exception as e:
        return handle_error(e, "get_step_status")


@app.route('/runs/<run_id>/<step_name>/logs', methods=['GET'])
def get_step_logs(run_id: str, step_name: str):
    """Get logs for a specific pipeline step."""
    try:
        if not validate_step_name(step_name):
            return {"error": f"Invalid step name: {step_name}"}, 400

        logs = job_utils.get_job_logs(run_id, step_name)
        return {"logs": logs}

    except Exception as e:
        return handle_error(e, "get_step_logs")


# ===============================
# RESULTS AND FILE DOWNLOADS
# ===============================

@app.route('/runs/<run_id>/results', methods=['GET'])
def get_all_results(run_id: str):
    """Get all results for a run."""
    try:
        # Check if run exists
        run_data = db.get_run(run_id)
        if not run_data:
            return {"error": f"Run not found: {run_id}"}, 404

        # Get all results for the run
        results = run_utils.get_run_results(run_id)

        return results

    except Exception as e:
        return handle_error(e, "get_all_results")


@app.route('/runs/<run_id>/results/<step>', methods=['GET'])
def get_step_results(run_id: str, step: str):
    """Get results for a specific pipeline step."""
    try:
        # Check if run exists
        run_data = db.get_run(run_id)
        if not run_data:
            return {"error": f"Run not found: {run_id}"}, 404

        # Get step-specific results
        results = run_utils.get_step_results(run_id, step)

        return results

    except Exception as e:
        return handle_error(e, "get_step_results")


@app.route('/runs/<run_id>/files/<path:file_path>', methods=['GET'])
def download_file(run_id: str, file_path: str):
    """Download a specific file from run workspace."""
    try:
        # Check if run exists
        run_data = db.get_run(run_id)
        if not run_data:
            return {"error": f"Run not found: {run_id}"}, 404

        # Get the actual file path (with security checks)
        actual_path = run_utils.get_run_files(run_id, file_path)

        # Send the file
        return send_file(actual_path, as_attachment=True)

    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}, 404
    except ValueError as e:
        return {"error": str(e)}, 400
    except Exception as e:
        return handle_error(e, "download_file")


@app.route('/runs/<run_id>/files', methods=['GET'])
def list_run_files(run_id: str):
    """List all files in run workspace."""
    try:
        # Check if run exists
        run_data = db.get_run(run_id)
        if not run_data:
            return {"error": f"Run not found: {run_id}"}, 404

        workspace = run_utils.RunWorkspace(run_id)
        if not workspace.exists():
            return {"error": f"Run workspace not found: {run_id}"}, 404

        # Get directory structure
        files = {}

        # List files in each subdirectory
        for subdir in run_utils.RUN_SUBDIRS:
            subdir_path = workspace.get_path(subdir)
            if os.path.exists(subdir_path):
                files[subdir] = []
                for item in os.listdir(subdir_path):
                    item_path = os.path.join(subdir_path, item)
                    if os.path.isfile(item_path):
                        # Get file info
                        stat = os.stat(item_path)
                        files[subdir].append({
                            "name": item,
                            "path": f"{subdir}/{item}",
                            "size": stat.st_size,
                            "modified": stat.st_mtime
                        })

        return {"files": files}

    except Exception as e:
        return handle_error(e, "list_run_files")


# ===============================
# JOB CONTROL ENDPOINTS
# ===============================

@app.route('/runs/<run_id>/kill', methods=['DELETE'])
def kill_run(run_id: str):
    """Kill all running jobs for a run."""
    try:
        # Check if run exists
        run_data = db.get_run(run_id)
        if not run_data:
            return {"error": f"Run not found: {run_id}"}, 404

        # Kill all running jobs for this run
        killed_count = job_utils.kill_run_jobs(run_id)

        # Update run status
        if killed_count > 0:
            db.update_run(run_id, status='killed', current_step=None)

        return {
            "message": f"Killed {killed_count} jobs for run {run_id}",
            "killed_jobs": killed_count
        }

    except Exception as e:
        return handle_error(e, "kill_run")


@app.route('/runs/<run_id>/clean', methods=['DELETE'])
def clean_run(run_id: str):
    """Clean up run workspace files (but keep database record)."""
    try:
        # Check if run exists
        run_data = db.get_run(run_id)
        if not run_data:
            return {"error": f"Run not found: {run_id}"}, 404

        # Kill any running jobs first
        killed_count = job_utils.kill_run_jobs(run_id)

        # Clean up workspace files
        success = run_utils.cleanup_run_workspace(run_id)

        # Update run status
        db.update_run(run_id, status='cleaned')

        return {
            "message": f"Cleaned workspace for run {run_id}",
            "files_deleted": success,
            "jobs_killed": killed_count
        }

    except Exception as e:
        return handle_error(e, "clean_run")


@app.route('/jobs/<int:job_id>/kill', methods=['DELETE'])
def kill_job(job_id: int):
    """Kill a specific job by ID."""
    try:
        # Get job info
        job = db.get_job(job_id)
        if not job:
            return {"error": f"Job not found: {job_id}"}, 404

        # Kill the job
        success = job_utils.kill_job_by_id(job_id)

        if success:
            return {
                "message": f"Job {job_id} killed successfully",
                "job_id": job_id,
                "run_id": job["run_id"]
            }
        else:
            return {"error": f"Failed to kill job {job_id}"}, 500

    except Exception as e:
        return handle_error(e, "kill_job")


# ===============================
# SYSTEM MANAGEMENT (ADDITIONAL)
# ===============================

@app.route('/system/cleanup', methods=['POST'])
def system_cleanup():
    """Clean up old logs and completed jobs."""
    try:
        days_old = request.json.get('days_old', 30) if request.json else 30

        # Clean up old job records
        jobs_cleaned = db.cleanup_completed_jobs(days_old)

        # Clean up old log files
        logs_cleaned = job_utils.cleanup_old_logs(days_old)

        return {
            "message": "System cleanup completed",
            "jobs_cleaned": jobs_cleaned,
            "logs_cleaned": logs_cleaned,
            "days_old": days_old
        }

    except Exception as e:
        return handle_error(e, "system_cleanup")


@app.route('/system/dependencies', methods=['GET'])
def system_dependencies():
    """Check system dependencies status."""
    try:
        deps = job_utils.get_system_dependencies()

        missing = [cmd for cmd, available in deps.items() if not available]
        available = [cmd for cmd, available in deps.items() if available]

        return {
            "dependencies": deps,
            "available": available,
            "missing": missing,
            "all_available": len(missing) == 0
        }

    except Exception as e:
        return handle_error(e, "system_dependencies")


# Initialize the application, needs to be here in order for it to work with flask & gunicorn
init_app()

if __name__ == '__main__':
    # Run the Flask development server
    print("Starting Flask development server...")
    app.run(host="0.0.0.0", port=5000, debug=True)
