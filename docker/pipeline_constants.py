"""
Constants for qsLAM PCR pipeline steps and configuration.

Canonical definitions shared across all modules to ensure consistency.
"""

# Pipeline step names (canonical list)
PIPELINE_STEPS = [
    'qc',           # FastQC quality control
    'umi',          # UMI processing
    'cutadapt',     # Adapter trimming
    'fastp',        # Alternative quality processing
    'readlen',      # Read length analysis
    'read_mapping', # BWA-MEM2 alignment
    'site_analysis' # Cutting site analysis and peak detection
]

# Valid step names for validation
VALID_STEP_NAMES = set(PIPELINE_STEPS)

# QC stages
QC_STAGES = ['before', 'after', 'both']

# Run status values
RUN_STATUSES = [
    'pending',      # Run created but no steps started
    'running',      # One or more steps currently executing
    'completed',    # All planned steps finished successfully
    'failed',       # One or more steps failed
    'killed'        # Run was manually terminated
]

# Job status values
JOB_STATUSES = [
    'pending',      # Job created but not started
    'running',      # Job currently executing
    'completed',    # Job finished successfully
    'failed',       # Job finished with errors
    'killed'        # Job was manually terminated
]

# Supported genome references with detailed configuration
SUPPORTED_GENOMES = {
    "GRCh38": {
        "fasta_file": "GRCh38.fa",
        "tar_url": "https://nc.liam-w.com/s/abXeB3WtcWdm63f/download?path=%2F&files=GRCh38.tar.gz"
    },
    "GRCh37": {
        "fasta_file": "GRCh37.fa",
        "tar_url": "https://nc.liam-w.com/s/abXeB3WtcWdm63f/download?path=%2F&files=GRCh37.tar.gz"
    },
    "GRCm39": {
        "fasta_file": "GRCm39.fa",
        "tar_url": "https://nc.liam-w.com/s/abXeB3WtcWdm63f/download?path=%2F&files=GRCm39.tar.gz"
    },
    "GRCm38": {
        "fasta_file": "GRCm38.fa",
        "tar_url": "https://nc.liam-w.com/s/abXeB3WtcWdm63f/download?path=%2F&files=GRCm38.tar.gz"
    },
    "MGSCv37": {
        "fasta_file": "MGSCv37.fa",
        "tar_url": "https://nc.liam-w.com/s/abXeB3WtcWdm63f/download?path=%2F&files=MGSCv37.tar.gz"
    }
}

def validate_step_name(step_name: str) -> bool:
    """Validate that step name is in canonical list."""
    return step_name in VALID_STEP_NAMES

def validate_run_status(status: str) -> bool:
    """Validate run status value."""
    return status in RUN_STATUSES

def validate_job_status(status: str) -> bool:
    """Validate job status value."""
    return status in JOB_STATUSES

def validate_genome(genome: str) -> bool:
    """Validate genome reference name."""
    return genome in SUPPORTED_GENOMES