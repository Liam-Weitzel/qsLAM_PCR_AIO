# qsLAM PCR AIO - Bruno API Test Collection

Manual API testing collection for the qsLAM PCR multi-run backend. Each
request corresponds to a backend endpoint and can be executed independently
through the Bruno UI.

## Prerequisites

- [Bruno](https://www.usebruno.com/) installed (desktop application)
- Python 3.x with Flask and dependencies installed
- The qsLAM PCR backend code in this repository

## Starting the Flask Server

From the `docker/` directory of this repository:

```bash
cd docker
python app.py
```

The server starts on `http://localhost:5000` by default. Verify it is running:

```bash
curl http://localhost:5000/health
```

## Creating Test FASTQ Files

For basic API testing (run creation, status checks, listing), you can use
minimal synthetic FASTQ files. These will allow you to verify API structure
and responses, though pipeline steps like cutadapt or read_mapping will fail
with synthetic data since they require real genomic reads.

Create small gzipped FASTQ files in the Bruno collection directory:

```bash
cd bruno

# Create a minimal R1 file (4 synthetic reads)
printf '@read1\nATCGATCGATCGATCGATCGATCGATCGATCGATCG\n+\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n@read2\nGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA\n+\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n@read3\nTTTTAAAACCCCGGGGTTTTAAAACCCCGGGGTTTT\n+\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n@read4\nAAAATTTTGGGGCCCCAAAATTTTGGGGCCCCAAAA\n+\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n' | gzip > test_R1.fastq.gz

# Create a minimal R2 file (4 synthetic reads)
printf '@read1\nCGATCGATCGATCGATCGATCGATCGATCGATCGAT\n+\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n@read2\nTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG\n+\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n@read3\nCCCCGGGGTTTTAAAACCCCGGGGTTTTAAAACCCC\n+\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n@read4\nGGGGCCCCAAAATTTTGGGGCCCCAAAATTTTGGGG\n+\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n' | gzip > test_R2.fastq.gz
```

These files are small enough to upload instantly but large enough to pass
basic file validation.

## Opening the Collection in Bruno

1. Open Bruno
2. Click "Open Collection"
3. Navigate to the `docker/bruno` directory in this repository
4. Select the folder -- Bruno will load the collection automatically

## Environment Variable Configuration

Select the **local** environment in the Bruno UI (top-right dropdown) before
executing any requests.

### Connection

| Variable | Default | Purpose |
|----------|---------|---------|
| `base_url` | `http://localhost:5000` | Flask server URL |
| `run_id` | (empty) | Set after creating a run |
| `job_id` | (empty) | Set when targeting a specific job |
| `step_name` | `qc` | Default step for status/logs queries |

### Genome

| Variable | Default | Purpose |
|----------|---------|---------|
| `test_genome` | `GRCh38` | Genome reference for read mapping and site analysis |

Supported genomes: GRCh38, GRCh37, GRCm39, GRCm38, MGSCv37.

### Cutadapt R1 Parameters

| Variable | Default | Purpose |
|----------|---------|---------|
| `r1_seq` | `ATCCCTCAGACCCTTTTAGTCAGTGTGGAAAATCTC` | R1 adapter sequence |
| `r1_error_rate` | `0.3` | Maximum error rate for R1 matching |
| `r1_trim_leading_trailing` | `0` | Bases to trim from R1 ends |
| `r1_anchored` | `false` | Whether R1 adapter is anchored (5' end) |
| `r1_min_overlap` | `5` | Minimum overlap for R1 adapter match |
| `r1_pair_filter` | `both` | Pair filter mode for R1 step |
| `r1_minimum_length_of_read` | `30` | Minimum read length after R1 trimming |

### Cutadapt R2 Parameters

| Variable | Default | Purpose |
|----------|---------|---------|
| `r2_seq` | `GACTGCGTATCAGT` | R2 adapter sequence |
| `r2_error_rate` | `0.1` | Maximum error rate for R2 matching |
| `r2_trim_leading_trailing` | `0` | Bases to trim from R2 ends |
| `r2_anchored` | `false` | Whether R2 adapter is anchored (5' end) |
| `r2_min_overlap` | `10` | Minimum overlap for R2 adapter match |
| `r2_pair_filter` | `both` | Pair filter mode for R2 step |
| `r2_minimum_length_of_read` | `30` | Minimum read length after R2 trimming |

### Site Analysis Parameters

| Variable | Default | Purpose |
|----------|---------|---------|
| `promoter_left` | `5000` | Bases upstream of TSS for promoter region |
| `promoter_right` | `2000` | Bases downstream of TSS for promoter region |
| `enhancer_left` | `50000` | Bases upstream for enhancer region search |

## Manual Workflow

The collection is designed for step-by-step manual execution. Here is the
typical workflow:

### 1. Create a Run

Open **Run Management / 01-Create Run** and execute it. This uploads FASTQ
files and stores all pipeline configuration. Use the Bruno UI file picker to
select your R1 and R2 files (the `@file()` paths in the request are
placeholders).

### 2. Copy the Run ID

From the response JSON, copy the `run_id` value (a UUID string).

### 3. Set the Run ID Environment Variable

In the Bruno UI, go to the **local** environment and paste the `run_id` value
into the `run_id` variable field. All subsequent requests use this variable.

### 4. Execute Pipeline Steps

Open the **Pipeline Steps** folder and execute steps in order:

1. Start QC Before (runs QC on raw uploaded reads)
2. Start Cutadapt (adapter trimming)
3. Start QC After (runs QC on trimmed reads)
4. Start Read Mapping
5. Start Site Analysis

Each step returns a `job_id` and starts processing in the background.

### 5. Check Step Status

Use **Pipeline Steps / Get Step Status** to poll for completion. Set the
`step_name` environment variable to the step you want to check (e.g.,
`cutadapt`, `read_mapping`, `site_analysis`).

### 6. View Results

Use the **Results and Files** folder to retrieve output files and analysis
results after steps complete.

## Important Notes

- The `@file()` paths in the Create Run request are placeholders. Use the
  Bruno UI file picker to select actual FASTQ files on your machine. Bruno
  does not support variable interpolation inside `@file()` paths.

- The `run_id` variable must be manually set after creating a run. It starts
  empty in the environment. If you see `{{run_id}}` literally in a URL, you
  forgot to set it.

- Pipeline steps run in the background and may take minutes to hours with
  real data. Use the status and logs endpoints to monitor progress.

- The QC step accepts a `?stage=before` or `?stage=after` query parameter
  to control whether it runs on raw reads or cutadapt-trimmed reads. You can
  call QC twice on the same run with different stages.

- Runs are not automatically deleted. Use the Delete Run or Clean Run
  Workspace requests when you are done inspecting results.

## Folder Organization

| Folder | Contents |
|--------|----------|
| **Run Management** | Create, list, get, delete runs; export/import config; kill jobs; clean workspace |
| **Pipeline Steps** | Start each pipeline step (QC, UMI, cutadapt, fastp, readlen, read mapping, site analysis) and check status/logs |
| **Results and Files** | Retrieve analysis results and download output files |
| **System** | Server info, health check, system status, genome list, dependencies, cleanup |

## Expected Execution Times

| Step | Synthetic Data | Small Dataset (~1M reads) | Large Dataset (~100M reads) |
|------|---------------|---------------------------|----------------------------|
| QC (FastQC) | Seconds | 1-2 minutes | 5-15 minutes |
| Cutadapt | Seconds | 1-5 minutes | 10-30 minutes |
| Fastp | Seconds | 1-3 minutes | 5-15 minutes |
| Read Mapping (BWA-MEM2) | Fails* | 5-15 minutes | 30-120 minutes |
| Site Analysis | Fails* | 5-10 minutes | 15-45 minutes |

*Read mapping and site analysis require real genomic data and a downloaded
reference genome to produce meaningful results. They will fail with synthetic
test data.
