"""
Run workspace management utilities for qsLAM PCR pipeline.

Handles isolated run directories with SHARED reference genomes:
runs/{run_id}/
├── rawdata/              # Input files (R1.fastq.gz, R2.fastq.gz)
├── cutPrimer/            # Trimmed reads
├── bwa/                  # Alignment outputs
├── fastqc/               # QC reports
│   ├── beforeCutAdapt/
│   └── afterCutAdapt/
├── bam2bed/              # Converted files
├── bed2peak/             # Peak analysis results
└── logs/                 # Step-specific log files

Global shared references:
reference/                # Shared genome files (2-8GB each)
├── GRCh38.fa            # Human genome reference
├── GRCh37.fa            # Human genome reference (legacy)
├── GRCm39.fa            # Mouse genome reference
├── GRCm38.fa            # Mouse genome reference (legacy)
└── MGSCv37.fa           # Mouse genome reference (older)
"""

import os
import shutil
import json
import uuid
import glob
from pathlib import Path
from typing import Dict, List, Optional, Any
from pipeline_constants import validate_step_name


# Run workspace subdirectories (NO reference subdir - uses shared)
RUN_SUBDIRS = [
    "rawdata",
    "cutPrimer",
    "bwa",
    "fastqc",
    "fastqc/beforeCutAdapt",
    "fastqc/afterCutAdapt",
    "bam2bed",
    "bed2peak",
    "readlen",
    "logs"
]

# Base directory for all runs
RUNS_BASE_DIR = "runs"

# Global shared reference directory
SHARED_REFERENCE_DIR = "reference"

# Import genome configuration from constants
from pipeline_constants import SUPPORTED_GENOMES

# BWA-MEM2 required index suffixes (from original api.py)
BWA_MEM2_INDEX_SUFFIXES = [
    ".0123",
    ".amb",
    ".ann",
    ".bwt.2bit.64",
    ".pac"
]


class RunWorkspace:
    """Manages workspace for a single run."""

    def __init__(self, run_id: str):
        self.run_id = run_id
        self.base_path = os.path.join(RUNS_BASE_DIR, run_id)

    def get_path(self, subdir: str = "", filename: str = "") -> str:
        """Get absolute path within run workspace."""
        if subdir and filename:
            return os.path.join(self.base_path, subdir, filename)
        elif subdir:
            return os.path.join(self.base_path, subdir)
        else:
            return self.base_path

    def get_rawdata_files(self) -> tuple[str, str]:
        """Get paths to R1 and R2 input files."""
        return (
            self.get_path("rawdata", "R1.fastq.gz"),
            self.get_path("rawdata", "R2.fastq.gz")
        )

    def get_cutadapt_files(self) -> tuple[str, str]:
        """Get paths to trimmed R1 and R2 files."""
        return (
            self.get_path("cutPrimer", "R1.fastq.gz"),
            self.get_path("cutPrimer", "R2.fastq.gz")
        )

    def get_bwa_files(self) -> dict[str, str]:
        """Get paths to alignment output files."""
        return {
            "sam": self.get_path("bwa", "aligned.sam"),
            "bam": self.get_path("bwa", "aligned.bam"),
            "sorted_bam": self.get_path("bwa", "aligned.sorted.bam"),
            "index": self.get_path("bwa", "aligned.sorted.bam.bai"),
            "stats": self.get_path("bwa", "aligned.stat")
        }

    def get_fastqc_output_dir(self, stage: str) -> str:
        """Get FastQC output directory for before/after stage."""
        if stage == "before":
            return self.get_path("fastqc", "beforeCutAdapt")
        elif stage == "after":
            return self.get_path("fastqc", "afterCutAdapt")
        else:
            raise ValueError(f"Invalid FastQC stage: {stage}")

    def get_shared_reference_path(self, genome: str) -> str:
        """Get path to shared reference genome FASTA file."""
        if genome not in SUPPORTED_GENOMES:
            raise ValueError(f"Unsupported genome: {genome}. Supported: {list(SUPPORTED_GENOMES.keys())}")
        return os.path.join(SHARED_REFERENCE_DIR, SUPPORTED_GENOMES[genome]["fasta_file"])

    def get_log_file(self, step_name: str) -> str:
        """Get log file path for a specific pipeline step."""
        return self.get_path("logs", f"{step_name}.log")

    def exists(self) -> bool:
        """Check if run workspace directory exists."""
        return os.path.exists(self.base_path)


def get_run_paths(run_id: str) -> Dict[str, str]:
    """Get all common paths for a run workspace."""
    workspace = RunWorkspace(run_id)
    r1_path, r2_path = workspace.get_rawdata_files()
    r1_cut, r2_cut = workspace.get_cutadapt_files()
    bwa_files = workspace.get_bwa_files()

    return {
        # Base paths
        "workspace": workspace.base_path,
        "rawdata": workspace.get_path("rawdata"),
        "cutPrimer": workspace.get_path("cutPrimer"),
        "bwa": workspace.get_path("bwa"),
        "fastqc": workspace.get_path("fastqc"),
        "fastqc_before": workspace.get_fastqc_output_dir("before"),
        "fastqc_after": workspace.get_fastqc_output_dir("after"),
        "bam2bed": workspace.get_path("bam2bed"),
        "bed2peak": workspace.get_path("bed2peak"),
        "logs": workspace.get_path("logs"),

        # Specific files
        "r1_input": r1_path,
        "r2_input": r2_path,
        "r1_trimmed": r1_cut,
        "r2_trimmed": r2_cut,
        "sam_file": bwa_files["sam"],
        "bam_file": bwa_files["bam"],
        "sorted_bam": bwa_files["sorted_bam"],
        "bam_index": bwa_files["index"],
        "bwa_stats": bwa_files["stats"],
        "readlen_pdf": workspace.get_path("readlen", "readlen.pdf")
    }


def get_run_workspace(run_id: str) -> RunWorkspace:
    """Get workspace for existing run."""
    workspace = RunWorkspace(run_id)
    if not workspace.exists():
        raise FileNotFoundError(f"Run workspace does not exist: {run_id}")
    return workspace


def list_run_workspaces() -> List[str]:
    """List all existing run IDs."""
    if not os.path.exists(RUNS_BASE_DIR):
        return []

    run_ids = []
    for item in os.listdir(RUNS_BASE_DIR):
        run_path = os.path.join(RUNS_BASE_DIR, item)
        if os.path.isdir(run_path):
            run_ids.append(item)

    return sorted(run_ids)


def cleanup_run_workspace(run_id: str) -> bool:
    """Delete all files and directories for a run."""
    workspace = RunWorkspace(run_id)

    if workspace.exists():
        try:
            shutil.rmtree(workspace.base_path)
            return True
        except Exception as e:
            raise RuntimeError(f"Failed to cleanup run workspace {run_id}: {str(e)}")

    return False


def save_uploaded_files(run_id: str, r1_file, r2_file) -> tuple[str, str]:
    """Save uploaded R1 and R2 files to run workspace."""
    workspace = get_run_workspace(run_id)

    # Ensure rawdata directory exists
    rawdata_dir = workspace.get_path("rawdata")
    os.makedirs(rawdata_dir, exist_ok=True)

    # Save files
    r1_path, r2_path = workspace.get_rawdata_files()
    r1_file.save(r1_path)
    r2_file.save(r2_path)

    return r1_path, r2_path


def get_run_files(run_id: str, file_path: str) -> str:
    """Get absolute path to file within run workspace."""
    workspace = get_run_workspace(run_id)

    # Security check: ensure path is within run workspace
    full_path = os.path.join(workspace.base_path, file_path)
    normalized_path = os.path.normpath(full_path)

    if not normalized_path.startswith(workspace.base_path):
        raise ValueError("File path outside run workspace")

    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    return normalized_path


def get_run_results(run_id: str) -> Dict[str, Any]:
    """Get all result files for a run."""
    workspace = get_run_workspace(run_id)
    results = {
        "bed2peak": {},
        "fastqc": {},
        "readlen_pdf": None,
        "bwa_stats": None
    }

    # Get bed2peak results
    bed2peak_dir = workspace.get_path("bed2peak")
    if os.path.exists(bed2peak_dir):
        results["bed2peak"] = _get_directory_contents(bed2peak_dir)

    # Get FastQC results
    fastqc_dir = workspace.get_path("fastqc")
    if os.path.exists(fastqc_dir):
        for stage_dir in ["beforeCutAdapt", "afterCutAdapt"]:
            stage_path = os.path.join(fastqc_dir, stage_dir)
            if os.path.exists(stage_path):
                results["fastqc"][stage_dir] = _get_directory_contents(stage_path)

    # Get readlen PDF if it exists
    readlen_pdf = workspace.get_path("readlen", "readlen.pdf")
    if os.path.exists(readlen_pdf):
        results["readlen_pdf"] = _encode_binary_file(readlen_pdf)

    # Get BWA stats
    bwa_stats = workspace.get_bwa_files()["stats"]
    if os.path.exists(bwa_stats):
        with open(bwa_stats, 'r') as f:
            results["bwa_stats"] = f.read()

    return results


def get_step_results(run_id: str, step: str) -> Dict[str, Any]:
    """Get results for a specific pipeline step."""
    # Validate step name
    if not validate_step_name(step):
        raise ValueError(f"Invalid step name: {step}")

    workspace = get_run_workspace(run_id)

    if step == "qc":
        results = {}
        fastqc_dir = workspace.get_path("fastqc")
        if os.path.exists(fastqc_dir):
            for stage_dir in ["beforeCutAdapt", "afterCutAdapt"]:
                stage_path = os.path.join(fastqc_dir, stage_dir)
                if os.path.exists(stage_path):
                    results[stage_dir] = _get_directory_contents(stage_path)
        return results

    elif step == "umi":
        # UMI results would go here when implemented
        return {}

    elif step == "cutadapt":
        return {
            "files": workspace.get_cutadapt_files(),
            "exists": [os.path.exists(f) for f in workspace.get_cutadapt_files()]
        }

    elif step == "fastp":
        # Fastp results would go here when implemented
        return {}

    elif step == "readlen":
        readlen_pdf = workspace.get_path("readlen", "readlen.pdf")
        if os.path.exists(readlen_pdf):
            return {"pdf": _encode_binary_file(readlen_pdf)}
        return {}

    elif step == "read_mapping":
        bwa_files = workspace.get_bwa_files()
        result = {"files": bwa_files}

        # Include stats if available
        if os.path.exists(bwa_files["stats"]):
            with open(bwa_files["stats"], 'r') as f:
                result["stats"] = f.read()

        return result

    elif step == "site_analysis":
        results = {}
        bed2peak_dir = workspace.get_path("bed2peak")
        if os.path.exists(bed2peak_dir):
            results["bed2peak"] = _get_directory_contents(bed2peak_dir)

        bam2bed_dir = workspace.get_path("bam2bed")
        if os.path.exists(bam2bed_dir):
            results["bam2bed"] = _get_directory_contents(bam2bed_dir)

        return results

    else:
        return {}


def export_run_config(run_id: str, run_data: Dict[str, Any]) -> Dict[str, Any]:
    """Export run configuration (no data files)."""
    export_data = {
        "export_version": "1.0",
        "run_id": run_id,
        "exported_at": None,  # This would be set by caller
        "config": {
            # Core run info
            "name": run_data.get("name"),
            "description": run_data.get("description"),
            "created_by": run_data.get("created_by"),

            # Cutadapt configuration
            "cutadapt": {
                "r1_seq": run_data.get("r1_seq"),
                "r1_error_rate": run_data.get("r1_error_rate"),
                "r1_trim_leading_trailing": run_data.get("r1_trim_leading_trailing"),
                "r1_anchored": run_data.get("r1_anchored"),
                "r1_min_overlap": run_data.get("r1_min_overlap"),
                "r1_pair_filter": run_data.get("r1_pair_filter"),
                "r1_minimum_length_of_read": run_data.get("r1_minimum_length_of_read"),
                "r2_seq": run_data.get("r2_seq"),
                "r2_error_rate": run_data.get("r2_error_rate"),
                "r2_trim_leading_trailing": run_data.get("r2_trim_leading_trailing"),
                "r2_anchored": run_data.get("r2_anchored"),
                "r2_min_overlap": run_data.get("r2_min_overlap"),
                "r2_pair_filter": run_data.get("r2_pair_filter"),
                "r2_minimum_length_of_read": run_data.get("r2_minimum_length_of_read")
            },

            # Read mapping configuration
            "read_mapping": {
                "genome": run_data.get("genome")
            },

            # Site analysis configuration
            "site_analysis": {
                "promoter_left": run_data.get("promoter_left"),
                "promoter_right": run_data.get("promoter_right"),
                "enhancer_left": run_data.get("enhancer_left")
            },

            # QC configuration
            "qc_stage": run_data.get("qc_stage")
        }
    }

    return export_data


def import_run_config(import_data: Dict[str, Any]) -> tuple[str, Dict[str, Any]]:
    """Import run configuration and return new run_id and config."""
    if import_data.get("export_version") != "1.0":
        raise ValueError("Unsupported export version")

    # Generate new run ID
    new_run_id = str(uuid.uuid4())

    # Extract configuration
    config = import_data.get("config", {})

    # Flatten configuration for database storage
    run_config = {
        "id": new_run_id,
        "name": config.get("name", "Imported Run"),
        "description": config.get("description"),
        "created_by": config.get("created_by"),
        "status": "pending"
    }

    # Add cutadapt config
    cutadapt_config = config.get("cutadapt", {})
    run_config.update({
        "r1_seq": cutadapt_config.get("r1_seq"),
        "r1_error_rate": cutadapt_config.get("r1_error_rate"),
        "r1_trim_leading_trailing": cutadapt_config.get("r1_trim_leading_trailing"),
        "r1_anchored": cutadapt_config.get("r1_anchored"),
        "r1_min_overlap": cutadapt_config.get("r1_min_overlap"),
        "r1_pair_filter": cutadapt_config.get("r1_pair_filter"),
        "r1_minimum_length_of_read": cutadapt_config.get("r1_minimum_length_of_read"),
        "r2_seq": cutadapt_config.get("r2_seq"),
        "r2_error_rate": cutadapt_config.get("r2_error_rate"),
        "r2_trim_leading_trailing": cutadapt_config.get("r2_trim_leading_trailing"),
        "r2_anchored": cutadapt_config.get("r2_anchored"),
        "r2_min_overlap": cutadapt_config.get("r2_min_overlap"),
        "r2_pair_filter": cutadapt_config.get("r2_pair_filter"),
        "r2_minimum_length_of_read": cutadapt_config.get("r2_minimum_length_of_read")
    })

    # Add read mapping config
    read_mapping_config = config.get("read_mapping", {})
    run_config.update({
        "genome": read_mapping_config.get("genome")
    })

    # Add site analysis config
    site_analysis_config = config.get("site_analysis", {})
    run_config.update({
        "promoter_left": site_analysis_config.get("promoter_left"),
        "promoter_right": site_analysis_config.get("promoter_right"),
        "enhancer_left": site_analysis_config.get("enhancer_left")
    })

    # Add QC config
    run_config["qc_stage"] = config.get("qc_stage")

    return new_run_id, run_config


def get_disk_usage() -> Dict[str, str]:
    """Get disk usage breakdown for runs and shared references."""
    runs_size = 0
    reference_size = 0

    # Calculate runs directory size
    if os.path.exists(RUNS_BASE_DIR):
        for root, dirs, files in os.walk(RUNS_BASE_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.exists(file_path):
                    runs_size += os.path.getsize(file_path)

    # Calculate shared reference directory size
    if os.path.exists(SHARED_REFERENCE_DIR):
        for root, dirs, files in os.walk(SHARED_REFERENCE_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.exists(file_path):
                    reference_size += os.path.getsize(file_path)

    def format_size(size: int) -> str:
        """Convert bytes to human readable format."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} PB"

    return {
        "runs": format_size(runs_size),
        "references": format_size(reference_size),
        "total": format_size(runs_size + reference_size)
    }


# Shared reference genome management

def ensure_shared_reference_dir() -> None:
    """Ensure shared reference directory exists."""
    os.makedirs(SHARED_REFERENCE_DIR, exist_ok=True)


def get_shared_reference_path(genome: str) -> str:
    """Get path to shared reference genome FASTA file."""
    if genome not in SUPPORTED_GENOMES:
        raise ValueError(f"Unsupported genome: {genome}. Supported: {list(SUPPORTED_GENOMES.keys())}")
    return os.path.join(SHARED_REFERENCE_DIR, SUPPORTED_GENOMES[genome]["fasta_file"])


def has_bwa_mem2_index(genome: str) -> bool:
    """Check if complete BWA-MEM2 index exists for genome (critical validation!)."""
    if genome not in SUPPORTED_GENOMES:
        return False

    fasta_path = get_shared_reference_path(genome)

    # Check if FASTA file exists first
    if not os.path.exists(fasta_path):
        return False

    # Check all required BWA-MEM2 index files exist
    for suffix in BWA_MEM2_INDEX_SUFFIXES:
        index_file = fasta_path + suffix
        if not os.path.exists(index_file):
            return False

    return True


def check_genome_available(genome: str) -> bool:
    """Check if complete BWA-MEM2 indexed genome is available."""
    return has_bwa_mem2_index(genome)


def download_genome_if_needed(genome: str) -> str:
    """Download and extract genome reference to shared directory if needed."""
    import subprocess
    import tarfile
    import urllib.request

    if genome not in SUPPORTED_GENOMES:
        raise ValueError(f"Unsupported genome: {genome}. Supported: {list(SUPPORTED_GENOMES.keys())}")

    tar_url = SUPPORTED_GENOMES[genome]["tar_url"]

    # Create shared reference directory if it doesn't exist
    os.makedirs(SHARED_REFERENCE_DIR, exist_ok=True)

    reference_path = get_shared_reference_path(genome)

    # If genome file already exists, return path
    if os.path.exists(reference_path):
        return reference_path

    # Download and extract genome
    tar_filename = f"{genome}.tar.gz"
    tar_path = os.path.join(SHARED_REFERENCE_DIR, tar_filename)

    try:
        # Download tar file
        print(f"Downloading {genome} reference from {tar_url}...")
        urllib.request.urlretrieve(tar_url, tar_path)

        # Extract tar file
        print(f"Extracting {tar_filename}...")
        with tarfile.open(tar_path, 'r:gz') as tar:
            tar.extractall(SHARED_REFERENCE_DIR)

        # Remove tar file after extraction
        os.remove(tar_path)

        # Verify extracted file exists
        if not os.path.exists(reference_path):
            raise FileNotFoundError(f"Expected reference file not found after extraction: {reference_path}")

        print(f"Successfully downloaded and extracted {genome} reference")
        return reference_path

    except Exception as e:
        # Clean up partial download
        if os.path.exists(tar_path):
            os.remove(tar_path)
        if os.path.exists(reference_path):
            os.remove(reference_path)
        raise RuntimeError(f"Failed to download genome {genome}: {str(e)}")


def get_genome_index_path(genome: str) -> str:
    """Get path to genome FASTA file for BWA-MEM2 (same as get_shared_reference_path)."""
    return get_shared_reference_path(genome)


def list_available_genomes() -> List[str]:
    """List all genomes with complete BWA-MEM2 indexes in shared directory."""
    if not os.path.exists(SHARED_REFERENCE_DIR):
        return []

    available = []
    for genome in SUPPORTED_GENOMES.keys():
        if has_bwa_mem2_index(genome):
            available.append(genome)

    return sorted(available)


def is_supported_genome(genome: str) -> bool:
    """Check if genome is in supported list."""
    return genome in SUPPORTED_GENOMES


def get_supported_genome_list() -> List[str]:
    """Get list of all supported genome names."""
    return list(SUPPORTED_GENOMES.keys())





def create_run_workspace(run_id: str) -> RunWorkspace:
    """Create directory structure for a new run (NO reference subdir)."""
    workspace = RunWorkspace(run_id)

    # Create base directory
    os.makedirs(workspace.base_path, exist_ok=True)

    # Create all subdirectories (excludes reference - uses shared)
    for subdir in RUN_SUBDIRS:
        os.makedirs(workspace.get_path(subdir), exist_ok=True)

    return workspace


# Helper functions

def _get_directory_contents(directory: str) -> Dict[str, Any]:
    """Get contents of directory with file type detection."""
    import mimetypes
    import base64

    contents = {}

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                mime_type, _ = mimetypes.guess_type(filepath)
                if mime_type and mime_type.startswith('text'):
                    # Text files - read as text
                    with open(filepath, 'r', encoding='utf-8') as f:
                        contents[filename] = {
                            "type": "text",
                            "content": f.read()
                        }
                else:
                    # Binary files - encode as base64
                    with open(filepath, 'rb') as f:
                        contents[filename] = {
                            "type": "binary",
                            "content": base64.b64encode(f.read()).decode('utf-8'),
                            "mime_type": mime_type or "application/octet-stream"
                        }
            except Exception as e:
                contents[filename] = {
                    "type": "error",
                    "error": str(e)
                }

    return contents


def _encode_binary_file(filepath: str) -> Dict[str, Any]:
    """Encode binary file as base64."""
    import base64
    import mimetypes

    mime_type, _ = mimetypes.guess_type(filepath)
    with open(filepath, 'rb') as f:
        return {
            "type": "binary",
            "content": base64.b64encode(f.read()).decode('utf-8'),
            "mime_type": mime_type or "application/octet-stream"
        }