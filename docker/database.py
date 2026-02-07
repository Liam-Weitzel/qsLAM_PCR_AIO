"""
Database module for qsLAM PCR pipeline.
Provides CRUD operations for runs and jobs tables using SQLite.
"""

import sqlite3
import uuid
from datetime import datetime
from typing import Optional, List, Dict, Any, Tuple
from contextlib import contextmanager
import os
from pipeline_constants import validate_genome


DB_FILE = "qslam.db"


@contextmanager
def get_db_connection():
    """Context manager for database connections with proper transaction handling."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # Enable dict-like row access
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key constraints
    try:
        yield conn
    except Exception:
        conn.rollback()
        raise
    else:
        conn.commit()
    finally:
        conn.close()


def init_database():
    """Initialize the database with the required schema."""
    with get_db_connection() as conn:
        # Create runs table with explicit columns (no JSON)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS runs (
                id TEXT PRIMARY KEY,
                name TEXT,
                description TEXT,
                status TEXT NOT NULL DEFAULT 'pending',
                current_step TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                created_by TEXT,

                -- Cutadapt configuration
                r1_seq TEXT,
                r1_error_rate REAL DEFAULT 0.3,
                r1_trim_leading_trailing INTEGER DEFAULT 0,
                r1_anchored BOOLEAN DEFAULT FALSE,
                r1_min_overlap INTEGER DEFAULT 5,
                r1_pair_filter TEXT DEFAULT 'both',
                r1_minimum_length_of_read INTEGER DEFAULT 30,
                r2_seq TEXT,
                r2_error_rate REAL DEFAULT 0.1,
                r2_trim_leading_trailing INTEGER DEFAULT 0,
                r2_anchored BOOLEAN DEFAULT FALSE,
                r2_min_overlap INTEGER DEFAULT 10,
                r2_pair_filter TEXT DEFAULT 'both',
                r2_minimum_length_of_read INTEGER DEFAULT 30,

                -- Read mapping configuration
                genome TEXT,

                -- Site analysis configuration
                promoter_left INTEGER DEFAULT 5000,
                promoter_right INTEGER DEFAULT 2000,
                enhancer_left INTEGER DEFAULT 50000,

                -- QC configuration
                qc_stage TEXT DEFAULT 'before'
            )
        """)

        # Create jobs table for execution history
        conn.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id TEXT NOT NULL,
                step_name TEXT NOT NULL,         -- qc, umi, cutadapt, fastp, readlen, read_mapping, site_analysis
                status TEXT NOT NULL DEFAULT 'pending',
                pgid INTEGER,
                started_at TIMESTAMP,
                completed_at TIMESTAMP,
                log_file TEXT,
                error_message TEXT,
                FOREIGN KEY (run_id) REFERENCES runs(id) ON DELETE CASCADE
            )
        """)


        # Create indexes for better query performance
        conn.execute("CREATE INDEX IF NOT EXISTS idx_runs_status ON runs(status)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_runs_created_by ON runs(created_by)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_runs_genome ON runs(genome)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_jobs_run_id ON jobs(run_id)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_jobs_step_name ON jobs(step_name)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_jobs_status ON jobs(status)")


def init_db():
    """Flask initialization function for database setup."""
    init_database()

    # Initialize shared reference directory
    from run_utils import ensure_shared_reference_dir
    ensure_shared_reference_dir()


# ===============================
# RUN CRUD OPERATIONS
# ===============================

def create_run(name: str, created_by: str = None, description: str = None, **config) -> str:
    """Create a new run with configuration parameters."""
    run_id = str(uuid.uuid4())

    # Validate genome if provided
    genome = config.get('genome')
    if genome:
        if not validate_genome(genome):
            from pipeline_constants import SUPPORTED_GENOMES
            supported = ", ".join(SUPPORTED_GENOMES.keys())
            raise ValueError(f"Unsupported genome '{genome}'. Supported genomes: {supported}")

    with get_db_connection() as conn:
        # Build the INSERT statement dynamically based on provided config
        base_fields = {
            'id': run_id,
            'name': name,
            'description': description,
            'created_by': created_by,
            'status': 'pending'
        }

        # Merge with config parameters
        all_fields = {**base_fields, **config}

        # Filter out None values
        fields = {k: v for k, v in all_fields.items() if v is not None}

        placeholders = ', '.join(['?' for _ in fields])
        field_names = ', '.join(fields.keys())

        conn.execute(
            f"INSERT INTO runs ({field_names}) VALUES ({placeholders})",
            list(fields.values())
        )

    return run_id


def get_run(run_id: str) -> Optional[Dict[str, Any]]:
    """Get a run by ID with all its configuration."""
    with get_db_connection() as conn:
        cursor = conn.execute("SELECT * FROM runs WHERE id = ?", (run_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def list_runs(created_by: str = None, limit: int = None) -> List[Dict[str, Any]]:
    """List all runs, optionally filtered by creator."""
    with get_db_connection() as conn:
        query = "SELECT * FROM runs"
        params = []

        if created_by:
            query += " WHERE created_by = ?"
            params.append(created_by)

        query += " ORDER BY created_at DESC"

        if limit:
            query += " LIMIT ?"
            params.append(limit)

        cursor = conn.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]


def update_run(run_id: str, **updates) -> bool:
    """Update a run with new values."""
    if not updates:
        return False

    # Always update the updated_at timestamp
    updates['updated_at'] = datetime.now().isoformat()

    with get_db_connection() as conn:
        # Filter out None values
        updates = {k: v for k, v in updates.items() if v is not None}

        if not updates:
            return False

        set_clause = ', '.join([f"{k} = ?" for k in updates.keys()])
        params = list(updates.values()) + [run_id]

        cursor = conn.execute(
            f"UPDATE runs SET {set_clause} WHERE id = ?",
            params
        )
        return cursor.rowcount > 0


def delete_run(run_id: str) -> bool:
    """Delete a run and all its associated jobs."""
    with get_db_connection() as conn:
        cursor = conn.execute("DELETE FROM runs WHERE id = ?", (run_id,))
        return cursor.rowcount > 0


def get_run_status(run_id: str) -> Optional[Dict[str, Any]]:
    """Get run status with step history."""
    run = get_run(run_id)
    if not run:
        return None

    # Get step history
    step_history = get_jobs_for_run(run_id)

    return {
        'run_id': run_id,
        'status': run['status'],
        'current_step': run['current_step'],
        'step_history': step_history
    }


# ===============================
# JOB CRUD OPERATIONS
# ===============================

def create_job(run_id: str, step_name: str, log_file: str = None) -> int:
    """Create a new job record."""
    with get_db_connection() as conn:
        cursor = conn.execute("""
            INSERT INTO jobs (run_id, step_name, log_file, status)
            VALUES (?, ?, ?, 'pending')
        """, (run_id, step_name, log_file))
        return cursor.lastrowid


def start_job(job_id: int, pgid: int = None) -> bool:
    """Mark a job as started with optional process group ID."""
    with get_db_connection() as conn:
        cursor = conn.execute("""
            UPDATE jobs
            SET status = 'running', started_at = CURRENT_TIMESTAMP, pgid = ?
            WHERE id = ?
        """, (pgid, job_id))
        return cursor.rowcount > 0


def complete_job(job_id: int, success: bool = True, error_message: str = None) -> bool:
    """Mark a job as completed or failed."""
    status = 'completed' if success else 'failed'

    with get_db_connection() as conn:
        cursor = conn.execute("""
            UPDATE jobs
            SET status = ?, completed_at = CURRENT_TIMESTAMP, error_message = ?
            WHERE id = ?
        """, (status, error_message, job_id))
        return cursor.rowcount > 0


def kill_job(job_id: int) -> bool:
    """Mark a job as killed."""
    with get_db_connection() as conn:
        cursor = conn.execute("""
            UPDATE jobs
            SET status = 'killed', completed_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (job_id,))
        return cursor.rowcount > 0


def get_job(job_id: int) -> Optional[Dict[str, Any]]:
    """Get a job by ID."""
    with get_db_connection() as conn:
        cursor = conn.execute("SELECT * FROM jobs WHERE id = ?", (job_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def get_jobs_for_run(run_id: str) -> List[Dict[str, Any]]:
    """Get all jobs for a run, ordered by creation time."""
    with get_db_connection() as conn:
        cursor = conn.execute("""
            SELECT * FROM jobs
            WHERE run_id = ?
            ORDER BY id ASC
        """, (run_id,))
        return [dict(row) for row in cursor.fetchall()]


def get_latest_job_for_step(run_id: str, step_name: str) -> Optional[Dict[str, Any]]:
    """Get the most recent job for a specific step in a run."""
    with get_db_connection() as conn:
        cursor = conn.execute("""
            SELECT * FROM jobs
            WHERE run_id = ? AND step_name = ?
            ORDER BY id DESC
            LIMIT 1
        """, (run_id, step_name))
        row = cursor.fetchone()
        return dict(row) if row else None


def get_running_jobs() -> List[Dict[str, Any]]:
    """Get all currently running jobs."""
    with get_db_connection() as conn:
        cursor = conn.execute("SELECT * FROM jobs WHERE status = 'running'")
        return [dict(row) for row in cursor.fetchall()]


def get_job_by_pgid(pgid: int) -> Optional[Dict[str, Any]]:
    """Get a job by its process group ID."""
    with get_db_connection() as conn:
        cursor = conn.execute("SELECT * FROM jobs WHERE pgid = ?", (pgid,))
        row = cursor.fetchone()
        return dict(row) if row else None



# ===============================
# UTILITY FUNCTIONS
# ===============================

def get_database_stats() -> Dict[str, Any]:
    """Get database statistics for system status."""
    with get_db_connection() as conn:
        # Get run counts by status
        cursor = conn.execute("""
            SELECT status, COUNT(*) as count
            FROM runs
            GROUP BY status
        """)
        run_stats = {row['status']: row['count'] for row in cursor.fetchall()}

        # Get active jobs count
        cursor = conn.execute("SELECT COUNT(*) as count FROM jobs WHERE status = 'running'")
        active_jobs = cursor.fetchone()['count']

        # Get total runs
        cursor = conn.execute("SELECT COUNT(*) as count FROM runs")
        total_runs = cursor.fetchone()['count']

        return {
            'total_runs': total_runs,
            'active_jobs': active_jobs,
            'run_stats': run_stats
        }


def cleanup_completed_jobs(days_old: int = 30) -> int:
    """Clean up job records older than specified days (but keep the runs)."""
    with get_db_connection() as conn:
        cursor = conn.execute("""
            DELETE FROM jobs
            WHERE status IN ('completed', 'failed', 'killed')
            AND completed_at < datetime('now', '-{} days')
        """.format(days_old))
        return cursor.rowcount


def export_run_config(run_id: str) -> Optional[Dict[str, Any]]:
    """Export run configuration for import on another server."""
    run = get_run(run_id)
    if not run:
        return None

    # Remove system fields that shouldn't be imported
    config = dict(run)
    for field in ['id', 'created_at', 'updated_at', 'status', 'current_step']:
        config.pop(field, None)

    return config


def import_run_config(config: Dict[str, Any], created_by: str = None) -> str:
    """Import run configuration from another server."""
    # Override created_by if provided
    if created_by:
        config['created_by'] = created_by

    return create_run(**config)