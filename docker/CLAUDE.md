# qsLAM PCR AIO Backend Refactor - Complete Implementation Guide

## Overview

Transform the qsLAM PCR pipeline from a single-run streaming architecture to a multi-run stateful backend with SQLite database. This enables concurrent users, team collaboration, and proper job management.

## Current State (Last Commit)

Starting from the old streaming architecture where:
- Single global directories (`rawdata/`, `cutPrimer/`, etc.)
- Streaming endpoints that block Flask workers for hours
- No concurrent user support
- Frontend manages state locally

## Target Architecture

### Core Principles
1. **Server-centric state management** - Backend owns all data and state
2. **Isolated run workspaces** - Each run gets `runs/{run_id}/` directory
3. **Non-blocking API** - Immediate responses, background job processing
4. **Flexible step execution** - No rigid dependencies, allow re-runs and experimentation
5. **Complete audit trail** - Track what steps were run, when, and their outcomes

### Database Schema (SQLite)

```sql
-- Core run tracking with explicit columns (no JSON)
CREATE TABLE runs (
    id TEXT PRIMARY KEY,              -- UUID
    name TEXT,                        -- User-friendly name
    description TEXT,                 -- Optional run description
    status TEXT NOT NULL DEFAULT 'pending',  -- overall run status
    current_step TEXT,                -- currently running step (null if none)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by TEXT,                  -- User identifier

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
    genome TEXT,                      -- hg38, mm10, etc.
    genome_tar_url TEXT,              -- Download URL for genome index

    -- Site analysis configuration
    promoter_left INTEGER DEFAULT 5000,
    promoter_right INTEGER DEFAULT 2000,
    enhancer_left INTEGER DEFAULT 50000,

    -- QC configuration
    qc_stage TEXT DEFAULT 'before'    -- before, after, both
);

-- Job execution history (allows multiple attempts per step)
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    step_name TEXT NOT NULL,         -- upload, qc_before, cutadapt, qc_after, read_mapping, site_analysis
    status TEXT NOT NULL DEFAULT 'pending',  -- pending, running, completed, failed, killed
    pgid INTEGER,                    -- process group ID for background jobs
    started_at TIMESTAMP,            -- when job was initiated
    completed_at TIMESTAMP,          -- when background process actually finished (null for sync jobs)
    log_file TEXT,                   -- path to log file
    error_message TEXT,
    FOREIGN KEY (run_id) REFERENCES runs(id) ON DELETE CASCADE
);
```

### Directory Structure

```
runs/
├── {run_id_1}/
│   ├── rawdata/              # Input files (R1.fastq.gz, R2.fastq.gz)
│   ├── cutPrimer/            # Trimmed reads
│   ├── bwa/                  # Alignment outputs
│   ├── fastqc/               # QC reports
│   │   ├── beforeCutAdapt/
│   │   └── afterCutAdapt/
│   ├── bam2bed/              # Converted files
│   ├── bed2peak/             # Peak analysis results
│   ├── reference/            # Downloaded genome references
│   └── logs/                 # Step-specific log files
├── {run_id_2}/
│   └── ...
qslam.db                      # SQLite database
```

## API Design

### 1. Run Management

#### Create Run with Upload (Combined)
```
POST /runs
Content-Type: multipart/form-data

Form fields:
- name: "My Experiment"
- R1: file upload
- R2: file upload
- config: JSON string with pipeline configuration

Response:
{
  "run_id": "uuid",
  "status": "upload_completed",
  "config_stored": ["cutadapt", "read_mapping", "site_analysis"]
}
```

#### List Runs
```
GET /runs
Response: {"runs": [run_objects...]}
```

#### Get Run Details
```
GET /runs/{id}
Response: {run object with jobs array}
```

#### Get Run Status with History
```
GET /runs/{id}/status
Response: {
  "run_id": "uuid",
  "status": "completed",
  "current_step": null,
  "step_history": [
    {"step_name": "upload", "status": "completed", "started_at": "..."},
    {"step_name": "qc_before", "status": "completed", "started_at": "..."},
    {"step_name": "qc_before", "status": "completed", "started_at": "..."}  // re-run
  ]
}
```

### 2. Pipeline Steps

All pipeline steps follow the same pattern:

#### Start Step
```
POST /runs/{id}/{step_name}
Response: {"job_id": 123, "status": "started"}
```

#### Get Step Status
```
GET /runs/{id}/{step_name}/status
Response: {"job_id": 123, "status": "completed", "started_at": "...", "error_message": null}
```

#### Get Step Logs
```
GET /runs/{id}/{step_name}/logs
Response: {"logs": "log content..."}
```

**Complete Pipeline Steps:**
- `qc` (FastQC quality control)
- `umi` (UMI processing)
- `cutadapt` (adapter trimming)
- `fastp` (alternative quality processing)
- `readlen` (read length analysis)
- `read_mapping` (BWA-MEM2 alignment)
- `site_analysis` (cutting site analysis and peak detection)

Note: Upload happens during run creation (`POST /runs`), not as a separate pipeline step.

### 3. Results and Files

#### Get All Results for Run
```
GET /runs/{id}/results
Response: {
  "bed2peak": {...},
  "fastqc": {...},
  "readlen_pdf": {...}
}
```

#### Get Step-Specific Results
```
GET /runs/{id}/results/{step}
Response: {step-specific files and data}
```

#### Download Specific File
```
GET /runs/{id}/files/{path}
Response: File download
```

### 4. Export/Import

#### Export Configuration
```
GET /runs/{id}/export
Response: JSON file download with configuration (no data files)
```

#### Import Configuration
```
POST /runs/import
Body: exported JSON configuration
Response: {"run_id": "new_uuid", "message": "Run imported successfully"}
```

### 5. Job Control

#### Kill Running Job
```
DELETE /runs/{id}/kill
Response: {"message": "Job killed", "job_id": 123}
```

#### Clean Run Files
```
DELETE /runs/{id}/clean
Response: {"message": "Run cleaned successfully", "files_deleted": true}
```

### 6. System Management

#### Server Status
```
GET /system/status
Response: {
  "active_jobs": 3,
  "total_runs": 15,
  "disk_usage": "2.3GB",
  "server_uptime": "2 days"
}
```

#### Server Info
```
GET /system/info
Response: {
  "name": "qsLAM PCR Server",
  "version": "2.0.0",
  "deployment_mode": "local|team|trial"
}
```

## Implementation Tasks

### Phase 1: Core Infrastructure
1. **Create SQLite database** with runs and jobs tables
2. **Implement run_utils.py** for directory management
3. **Implement database.py** with all CRUD operations
4. **Create job_utils.py** for background process management
5. **Update api.py imports** to use new modules

### Phase 2: Run Management API
1. **Implement combined run creation + upload** (`POST /runs`)
2. **Add run listing and details** (`GET /runs`, `GET /runs/{id}`)
3. **Add run status with step history** (`GET /runs/{id}/status`)
4. **Add export/import functionality** (`GET /runs/{id}/export`, `POST /runs/import`)
5. **Add job control** (`DELETE /runs/{id}/kill`, `DELETE /runs/{id}/clean`)

### Phase 3: Pipeline Steps Implementation
1. **Implement QC endpoint** - `/runs/{id}/qc` with run-specific directories
2. **Implement UMI endpoint** - `/runs/{id}/umi` with background job processing
3. **Implement cutadapt endpoint** - `/runs/{id}/cutadapt` with run-specific paths
4. **Implement fastp endpoint** - `/runs/{id}/fastp` with background job processing
5. **Implement readlen endpoint** - `/runs/{id}/readlen` with run-specific paths
6. **Implement read_mapping endpoint** - `/runs/{id}/read_mapping` with proper path handling
7. **Implement site_analysis endpoint** - `/runs/{id}/site_analysis` with complex subprocess commands

### Phase 4: Results and Files
1. **Implement run-specific results** (`GET /runs/{id}/results`)
2. **Add step-specific results** (`GET /runs/{id}/results/{step}`)
3. **Add file download** (`GET /runs/{id}/files/{path}`)
4. **Remove legacy get_results** - Replace with run-specific version

### Phase 5: System Management
1. **Add system status endpoint** - Active jobs, disk usage, server health
2. **Add system info endpoint** - Server name, version, capabilities
3. **Add cleanup functionality** - Auto-cleanup old runs



## Background Job Management Design

### Process Execution Pattern
```python
def start_background_job(run_id, step_name, cmd, paths):
    log_file = get_log_file_path(run_id, step_name)
    job_id = create_job(run_id, step_name, log_file)

    # Start background process with PGID tracking
    process = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid, ...)
    pgid = os.getpgid(process.pid)
    start_job(job_id, pgid)
    update_run(run_id, status='running', current_step=step_name)

    # Start monitor thread
    threading.Thread(target=monitor_completion, args=(process, job_id)).start()

    return job_id
```

### Monitor Thread Responsibilities
1. Stream process output to log file
2. Wait for process completion
3. Update job status (completed/failed) based on exit code
4. Update run status and reset current_step
5. Handle process errors and cleanup

## Configuration Management

### Run Creation Request Format
```bash
# Create run with all configuration as form fields
curl -X POST http://localhost:5000/runs \
  -F "name=My Experiment" \
  -F "description=Testing new parameters" \
  -F "created_by=researcher@lab.com" \
  -F "R1=@test_R1.fastq.gz" \
  -F "R2=@test_R2.fastq.gz" \
  -F "r1_seq=ATCCCTCAGACCCTTTTAGTCAGTGTGGAAAATCTC" \
  -F "r1_error_rate=0.3" \
  -F "r1_anchored=false" \
  -F "r2_seq=GACTGCGTATCAGT" \
  -F "r2_error_rate=0.1" \
  -F "genome=hg38" \
  -F "genome_tar_url=https://example.com/hg38.tar.gz" \
  -F "promoter_left=5000" \
  -F "promoter_right=2000" \
  -F "enhancer_left=50000" \
  -F "qc_stage=before"
```

**Benefits of normalized schema:**
- No JSON parsing/serialization
- Proper data types (INTEGER, REAL, BOOLEAN)
- Easy SQL queries: `SELECT * FROM runs WHERE genome = 'hg38'`
- Frontend can submit as form fields
- Better export/import (just database rows)

## Testing Strategy

### 1. Basic Flow Testing
```bash
# Create run with upload
curl -X POST http://localhost:5000/runs \
  -F "name=Test Run" \
  -F "R1=@test_R1.fastq.gz" \
  -F "R2=@test_R2.fastq.gz" \
  -F 'config={"cutadapt":{"r1_seq":"ATCG","r2_seq":"GCTA"},...}'

# Run pipeline steps
curl -X POST http://localhost:5000/runs/{id}/qc
curl -X POST http://localhost:5000/runs/{id}/cutadapt
curl -X POST http://localhost:5000/runs/{id}/read_mapping
curl -X POST http://localhost:5000/runs/{id}/site_analysis

# Check status and history
curl http://localhost:5000/runs/{id}/status
curl http://localhost:5000/runs/{id}/results
```

### 2. Re-run Testing
```bash
# Re-run steps (should work without dependencies)
curl -X POST http://localhost:5000/runs/{id}/qc  # Run QC again
curl -X POST http://localhost:5000/runs/{id}/cutadapt  # Run cutadapt again
curl http://localhost:5000/runs/{id}/status  # Should show multiple attempts
```

### 3. Multi-user Testing
```bash
# Create multiple runs simultaneously
curl -X POST ... # User 1 creates run A
curl -X POST ... # User 2 creates run B
curl -X POST http://localhost:5000/runs/{run_A}/qc &
curl -X POST http://localhost:5000/runs/{run_B}/cutadapt &
# Both should run concurrently without conflicts
```

## Implementation Priority

Starting fresh from the last commit (before refactor attempts):

### Phase 1: Foundation (Implement First)
1. **Create SQLite database** - Normalized schema with individual columns
2. **Implement database.py** - All CRUD operations for runs and jobs
3. **Implement run_utils.py** - Directory management for isolated workspaces
4. **Implement job_utils.py** - Background process management with monitor threads

### Phase 2: Core API (Essential)
1. **Run management endpoints** - Create, list, get, delete runs
2. **Combined run creation + upload** - Single endpoint for config + files
3. **Job control** - Kill and cleanup operations
4. **Export/import** - Configuration migration between servers

### Phase 3: Pipeline Implementation (Complete Workflow)
1. **All 7 pipeline steps** - QC, UMI, cutadapt, fastp, readlen, read_mapping, site_analysis
2. **Run-specific paths** - All subprocess commands use `runs/{id}/` directories
3. **Background job processing** - Monitor threads update complete job status and database state

### Phase 4: Results and System Management (Polish)
1. **Results endpoints** - Run-specific results instead of global
2. **File download** - Access individual run files
3. **System management** - Server status and health monitoring

## Key Design Decisions

### Why No Step Dependencies?
Users need flexibility to:
- Re-run steps with different parameters
- Skip certain steps entirely
- Experiment with different workflows
- Debug specific pipeline components

The system tracks what happened (audit trail) rather than enforcing what should happen.

### Why Monitor Threads?
- Background processes need completion tracking
- Frontend needs to know when jobs finish
- Proper process cleanup and resource management
- Real-time status updates without constant polling

## Success Criteria

### Functional Requirements
- [ ] Multiple users can run pipelines simultaneously without conflicts
- [ ] All steps can be re-run multiple times
- [ ] Complete step history available for debugging
- [ ] Export/import works between servers
- [ ] Background jobs can be killed properly
- [ ] All file operations use isolated run directories

### Performance Requirements
- [ ] API responses are immediate (non-blocking)
- [ ] No Flask worker blocking during long operations
- [ ] Concurrent job execution supported
- [ ] Proper resource cleanup

### Data Safety Requirements
- [ ] SQLite ACID transactions prevent corruption
- [ ] Process crashes don't affect other runs
- [ ] All state survives server restarts
- [ ] Complete audit trail for reproducibility

## Frontend Architecture Notes

The frontend will adopt the same server-centric model - users connect to servers and work with runs that exist on those servers. No backward compatibility needed as both frontend and backend are being updated together to the new architecture.

## Implementation Notes for Claude

**Act as Implementation Manager:**
- Use the Task tool extensively to launch specialized agents for complex implementations
- Break down large tasks into multiple concurrent agent operations
- Delegate database schema creation, API endpoint implementation, and testing to subagents
- Coordinate multiple agents working in parallel on different components
- Focus on high-level orchestration rather than manual coding

**Agent Delegation Strategy:**
- **Database agent**: Schema creation and migration scripts
- **API agent**: Endpoint implementation with proper error handling
- **Testing agent**: Comprehensive testing of new endpoints
- **File management agent**: Directory structure and path utilities
- **Background job agent**: Process management and monitor thread implementation

**Key Implementation Principles:**
1. **Start from last commit** - Revert current changes and implement clean architecture
2. **Use normalized database** - No JSON in database, proper column types
3. **Monitor threads manage complete job lifecycle** - Update job status, run status, and completion times when background processes finish
4. **Complete implementation** - All 7 pipeline steps with run-specific paths

This comprehensive refactor will transform the system from single-user blocking to multi-user concurrent with powerful new capabilities for collaboration and experimentation.
