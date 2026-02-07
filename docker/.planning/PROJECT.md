# qsLAM PCR AIO Backend Refactor

## What This Is

A multi-run stateful backend for the qsLAM PCR bioinformatics pipeline. Transforms the existing single-run streaming architecture into a concurrent, database-backed system where multiple users can run pipeline steps independently with isolated workspaces. Built with Flask, SQLite, and background job processing.

## Core Value

Multiple users can run concurrent pipelines on the same backend without interfering with each other — every run gets isolated workspace directories and its own job history.

## Requirements

### Validated

- ✓ SQLite database with normalized schema (runs + jobs tables) — existing
- ✓ Run workspace isolation (`runs/{run_id}/` directories) — existing
- ✓ Background job execution with monitor threads and PGID tracking — existing
- ✓ Non-blocking API (immediate responses, background processing) — existing
- ✓ Run management endpoints (create, list, get, delete, export, import) — existing
- ✓ QC step (FastQC before/after) — existing
- ✓ Cutadapt step (2-pass primer trimming) — existing
- ✓ Fastp step (quality processing) — existing
- ✓ Read mapping step (BWA-MEM2 with genome download) — existing
- ✓ Job control (kill running jobs, clean run files) — existing
- ✓ System status and info endpoints — existing
- ✓ Results retrieval and file download endpoints — existing
- ✓ Shell scripts parameterized for run workspaces (all_peaks.sh, merge_peaks.sh, deduplicate_bed.sh) — existing
- ✓ Perl scripts parameterized (filter_reads.pl, bedpe_to_bed.pl) — existing
- ✓ R annotation scripts parameterized (peak_annotation_step1.R, peak_annotation_step2.R) — existing

### Active

- [ ] Port site analysis pipeline from old API to new run-workspace architecture
- [ ] Fix hardcoded output path in readlen_analysis.R (`pdf("readLen.pdf")` writes to CWD, not run directory)
- [ ] Fix relative `source()` path in peak_annotation_step1.R for target_gene_prediction.R
- [ ] Remove `genome_tar_url` from user-facing API — look up from SUPPORTED_GENOMES constants instead
- [ ] Remove `genome_tar_url` column from database schema
- [ ] Set up Bruno API test collections covering the full workflow
- [ ] Commit all refactor work on `rewrite` branch

### Out of Scope

- Authentication/authorization — not needed for lab deployment
- Frontend changes — frontend will be updated separately to match new API
- UMI processing implementation — keep as stub, not needed for current workflows
- Automated test suite (pytest) — using Bruno for manual API testing instead
- Command injection hardening — address in a follow-up pass

## Context

- **Starting point:** Old streaming API (`api_old_streaming.py`) with global directories, single-run, blocking endpoints
- **Current state:** Refactor ~95% complete but uncommitted and untested. New architecture in `app.py`, `database.py`, `job_utils.py`, `run_utils.py`, `pipeline_constants.py`
- **Site analysis gap:** The old API has a complete working implementation (bam2bed, bed2peak, R annotation pipeline) that needs to be adapted to use run workspaces and the new job execution pattern
- **R/Perl scripts:** Most are already parameterized via command-line args. Two have hardcoded path issues (readlen output, peak_annotation source path)
- **Genome URL cleanup:** `pipeline_constants.py` already has `SUPPORTED_GENOMES` with tar URLs mapped per genome. The `genome_tar_url` field in the DB schema and API is redundant
- **Version control:** Working on `rewrite` branch, will merge to `master` when tested

## Constraints

- **Tech stack**: Python/Flask/SQLite, R, Perl, Bash — all managed via Nix flake
- **Deployment**: Docker container with NixOS base image
- **Compatibility**: Must support 5 genomes (GRCh38, GRCh37, GRCm39, GRCm38, MGSCv37)
- **Storage**: Large files (fastq.gz uploads, genome references up to 8GB each)
- **Concurrency**: Multiple simultaneous runs, one active step per run

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Normalized DB schema (no JSON) | Proper types, easy queries, form field submission | ✓ Good |
| Shared genome reference directory | Avoid duplicating multi-GB genome files per run | ✓ Good |
| Monitor threads for job completion | Need async completion tracking without polling | ✓ Good |
| No step dependencies enforced | Users need flexibility to re-run and experiment | ✓ Good |
| Keep UMI as stub | Not needed for current lab workflows | — Pending |
| Bruno for testing over pytest | Manual API testing sufficient for this stage | — Pending |
| Work on rewrite branch | Don't risk master with large uncommitted refactor | — Pending |

---
*Last updated: 2026-02-07 after initialization*
