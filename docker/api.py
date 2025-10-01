from flask import Flask, request, jsonify, stream_with_context, Response
import os, subprocess, multiprocessing

app = Flask(__name__)

#TODO: Return actual status codes
# Use safe stream
# Max defensive programming
# Testing

NUM_THREADS = multiprocessing.cpu_count()
RAW_DIR = "rawdata"
CUT_DIR = "cutPrimer"
BWA_DIR = "bwa"
FASTQC_BEFORE_OUT = "fastqc/beforeCutAdapt"
FASTQC_AFTER_OUT  = "fastqc/afterCutAdapt"
R1_FILE = os.path.join(RAW_DIR, "R1.fastq.gz")
R2_FILE = os.path.join(RAW_DIR, "R2.fastq.gz")
REFERENCE = "reference"

@app.route('/')
def index():
    return jsonify(message="Hello from qsLAM_PCR_AIO!")

def stream_cmd(cmd, cwd=None):
    """Run a command and yield stdout+stderr lines in real time with feedback markers."""
    yield f"[INFO] Running: {' '.join(cmd)}\n"
    p = subprocess.Popen(
        cmd,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    for line in p.stdout:
        yield f"[LOG] {line}"
    p.wait()
    if p.returncode == 0:
        yield f"[DONE] {cmd[0]} finished successfully\n"
    else:
        yield f"[ERROR] {cmd[0]} exited with code {p.returncode}\n"

@app.route('/upload_r1_r2', methods=['POST'])
def upload_r1_r2():
    """
    curl -N -X POST http://localhost:5000/upload_r1_r2 \
      -F "R1=@/home/liam-w/qsLAM_PCR_AIO/docker/rawdata/R1.fastq.gz" \
      -F "R2=@/home/liam-w/qsLAM_PCR_AIO/docker/rawdata/R2.fastq.gz"
    """
    @stream_with_context
    def gen():
        os.makedirs(RAW_DIR, exist_ok=True)

        if 'R1' not in request.files or 'R2' not in request.files:
            yield "[ERROR] Please upload both R1 and R2 files\n"
            return

        r1_file = request.files['R1']
        r2_file = request.files['R2']

        yield "[INFO] Saving R1 file…\n"
        r1_file.save(R1_FILE)
        yield f"[DONE] R1 saved to {R1_FILE}\n"

        yield "[INFO] Saving R2 file…\n"
        r2_file.save(R2_FILE)
        yield f"[DONE] R2 saved to {R2_FILE}\n"

        yield "✅ Upload successful\n"

    return Response(gen(), mimetype="text/plain")

@app.route('/qc', methods=['POST'])
def qc():
    """
    curl -N -X POST http://localhost:5000/qc \
      -H "Content-Type: application/json" \
      -d '{"stage": "before"}'
    or
    curl -N -X POST http://localhost:5000/qc \
      -H "Content-Type: application/json" \
      -d '{"stage": "after"}'
    """
    params = request.get_json(force=True)
    stage = params.get("stage", "before")

    @stream_with_context
    def gen():
        if stage == "before":
            outdir = FASTQC_BEFORE_OUT
            r1, r2 = R1_FILE, R2_FILE
        elif stage == "after":
            outdir = FASTQC_AFTER_OUT
            r1 = os.path.join(CUT_DIR, "R1.fastq.gz")
            r2 = os.path.join(CUT_DIR, "R2.fastq.gz")
        else:
            yield f"[ERROR] Unknown stage: {stage}\n"
            return

        os.makedirs(outdir, exist_ok=True)
        yield f"[INFO] Running FastQC ({stage})…\n"
        yield from stream_cmd(["fastqc", "-o", outdir, r1])
        yield from stream_cmd(["fastqc", "-o", outdir, r2])
        yield f"✅ QC ({stage}) complete\n"

    return Response(gen(), mimetype="text/plain")

@app.route('/umi', methods=['GET'])
def umi():
    """
    curl http://localhost:5000/umi
    """
    @stream_with_context
    def gen():
        yield "[INFO] UMI step not implemented yet.\n"
    return Response(gen(), mimetype="text/plain")

@app.route('/cutadapt', methods=['POST'])
def cutadapt():
    """
    curl -N -X POST http://localhost:5000/cutadapt \
      -H "Content-Type: application/json" \
      -d '{
        "r1_seq": "ATCCCTCAGACCCTTTTAGTCAGTGTGGAAAATCTC",
        "r2_seq": "GACTGCGTATCAGT",
        "r1_error_rate": 0.1,
        "r1_trim_leading_trailing": 0,
        "r1_anchored": false,
        "r1_min_overlap": 0,
        "r1_pair_filter": "both",
        "r1_minimum_length_of_read": 30,
        "r2_error_rate": 0.1,
        "r2_trim_leading_trailing": 0,
        "r2_anchored": false,
        "r2_min_overlap": 10,
        "r2_pair_filter": "both",
        "r2_minimum_length_of_read": 30
      }'
    """
    params = request.get_json(force=True)

    @stream_with_context
    def gen():
        os.makedirs(CUT_DIR, exist_ok=True)

        r1_seq  = params["r1_seq"]
        r2_seq  = params["r2_seq"]

        tmp1 = os.path.join(CUT_DIR, "step1_R1.fastq.gz")
        tmp2 = os.path.join(CUT_DIR, "step1_R2.fastq.gz")
        out1 = os.path.join(CUT_DIR, "R1.fastq.gz")
        out2 = os.path.join(CUT_DIR, "R2.fastq.gz")

        yield "[INFO] Cutadapt step 1…\n"
        yield from stream_cmd([
            "cutadapt",
            "-e", str(params["r1_error_rate"]),
            "--cut", str(params["r1_trim_leading_trailing"]),
            "-g", f"{'^' if params['r1_anchored'] else ''}{r1_seq};min_overlap={params['r1_min_overlap']}",
            "--pair-filter", params["r1_pair_filter"],
            "-m", str(params["r1_minimum_length_of_read"]),
            "-j", str(NUM_THREADS),
            "-o", tmp1,
            "-p", tmp2,
            R1_FILE,
            R2_FILE
        ])

        yield "[INFO] Cutadapt step 2…\n"
        yield from stream_cmd([
            "cutadapt",
            "-e", str(params["r2_error_rate"]),
            "--cut", str(params["r2_trim_leading_trailing"]),
            "-G", f"{'^' if params['r2_anchored'] else ''}{r2_seq};min_overlap={params['r2_min_overlap']}",
            "--pair-filter", params["r2_pair_filter"],
            "-m", str(params["r2_minimum_length_of_read"]),
            "-j", str(NUM_THREADS),
            "-o", out1,
            "-p", out2,
            tmp1,
            tmp2
        ])

        os.remove(tmp1)
        os.remove(tmp2)
        yield "✅ Cutadapt complete\n"

    return Response(gen(), mimetype="text/plain")

@app.route('/fastp', methods=['GET'])
def fastp():
    """
    curl http://localhost:5000/fastp
    """
    @stream_with_context
    def gen():
        tmp_r1 = os.path.join(RAW_DIR, "R1.fastp.fastq.gz")
        tmp_r2 = os.path.join(RAW_DIR, "R2.fastp.fastq.gz")

        yield "[INFO] Running fastp…\n"
        yield from stream_cmd([
            "fastp",
            "-i", R1_FILE,
            "-I", R2_FILE,
            "-o", tmp_r1,
            "-O", tmp_r2
        ])
        yield f"[DONE] fastp complete → {tmp_r1}, {tmp_r2}\n"
    return Response(gen(), mimetype="text/plain")

@app.route('/readlen', methods=['GET'])
def readlen():
    """
    curl http://localhost:5000/readlen
    """
    @stream_with_context
    def gen():
        r1 = os.path.join(CUT_DIR, "R1.fastq.gz")
        r2 = os.path.join(CUT_DIR, "R2.fastq.gz")

        yield "[INFO] Running readlen analysis…\n"
        yield from stream_cmd(["Rscript", "readlen_analysis.R", r1, r2])
        yield "✅ Readlen analysis complete\n"
    return Response(gen(), mimetype="text/plain")

# BWA-MEM2 required index suffixes
required_suffixes = [
    ".0123",
    ".amb",
    ".ann",
    ".bwt.2bit.64",
    ".pac"
]

def has_bwa_mem2_index(idx_fa):
    return all(os.path.isfile(idx_fa + s) for s in required_suffixes)

@app.route('/upload_ref_genome', methods=['POST'])
def upload_ref_genome():
    """
    curl -N -X POST http://localhost:5000/upload_ref_genome \\
      -F "REF=@/path/to/local/reference_genome.tar.gz" \\
      -F "NAME=test"
    """
    @stream_with_context
    def gen():
        os.makedirs(REFERENCE, exist_ok=True)

        if 'REF' not in request.files:
            yield "[ERROR] Please upload the reference genome (field: REF)\n"
            return
        if 'NAME' not in request.form:
            yield "[ERROR] Please provide a NAME field\n"
            return

        ref_file = request.files['REF']
        ref_name = request.form['NAME']
        idx_fa = os.path.join(REFERENCE, f"{ref_name}.fa")

        # Check if all index files already exist
        if has_bwa_mem2_index(idx_fa):
            yield f"[INFO] Reference genome {ref_name} with all BWA-MEM2 index files already exists. Skipping upload and extraction.\n"
            yield "✅ Ready for read mapping\n"
            return

        tar_path = os.path.join(REFERENCE, f"{ref_name}.fa.tar.gz")
        yield f"[INFO] Saving uploaded file as {tar_path}…\n"
        ref_file.save(tar_path)
        yield "[DONE] File saved\n"

        yield f"[INFO] Extracting {tar_path} into {REFERENCE}…\n"
        yield from stream_cmd(["tar", "-xzf", tar_path, "-C", REFERENCE])
        os.remove(tar_path)
        yield "[DONE] Extraction complete\n"

        # Check for missing BWA-MEM2 index files
        missing = [s for s in required_suffixes if not os.path.isfile(idx_fa + s)]
        if missing:
            yield f"[WARNING] Missing BWA-MEM2 index files for {ref_name}: {', '.join(missing)}\n"
            yield "[INFO] You will need to generate or download the missing indices before read mapping.\n"
        else:
            yield f"[INFO] All BWA-MEM2 index files present for {ref_name}\n"

        yield f"✅ Reference genome uploaded and extracted: {ref_name}\n"

    return Response(gen(), mimetype="text/plain")

@app.route('/get_ref_genomes', methods=['GET'])
def get_ref_genomes():
    """
    curl http://localhost:5000/get_ref_genomes
    """
    GENOME_DIR = "reference"
    os.makedirs(GENOME_DIR, exist_ok=True)

    genomes = set()
    for fname in os.listdir(GENOME_DIR):
        if ".fa" in fname and not fname.endswith(".tar.gz"):
            idx_fa = os.path.join(GENOME_DIR, fname)
            if has_bwa_mem2_index(idx_fa):
                genomes.add(fname)

    return jsonify({
        "ref_genomes": sorted(genomes),
        "count": len(genomes)
    })

@app.route('/read_mapping', methods=['POST'])
def read_mapping():
    """
    curl -N -X POST http://localhost:5000/read_mapping \
      -H "Content-Type: application/json" \
      -d '{
        "genome": "GRCh38.p14",
        "tar_url": "https://nc.liam-w.com/s/abXeB3WtcWdm63f/download?path=%2F&files=GRCh38.p14.tar.gz"
      }'
    """
    params = request.get_json(force=True)
    genome = params["genome"]
    tar_url = params["tar_url"]

    @stream_with_context
    def gen():
        os.makedirs(REFERENCE, exist_ok=True)
        os.makedirs(BWA_DIR, exist_ok=True)

        idx_fa = os.path.join(REFERENCE, f"{genome}.fa")
        CUT_R1_FILE = os.path.join(CUT_DIR, "R1.fastq.gz")
        CUT_R2_FILE = os.path.join(CUT_DIR, "R2.fastq.gz")

        # Check if all bwa-mem2 index files exist
        if not has_bwa_mem2_index(idx_fa):
            yield f"📥 Downloading {genome} BWA-MEM2 index from {tar_url}…\n"
            tar_path = os.path.join(REFERENCE, f"{genome}.tar.gz")
            yield from stream_cmd(["wget", tar_url, "-O", tar_path])
            yield from stream_cmd(["tar", "-xzf", tar_path, "-C", REFERENCE])
            os.remove(tar_path)
            yield "Download & extraction complete\n"

        yield f"🧬 Aligning reads using {genome}…\n"
        sam_out = os.path.join(BWA_DIR, "aligned.sam")
        yield from stream_cmd([
            "bwa-mem2", "mem", "-t", str(NUM_THREADS),
            idx_fa, CUT_R1_FILE, CUT_R2_FILE, "-o", sam_out
        ])

        bam_out = os.path.join(BWA_DIR, "aligned.bam")
        yield from stream_cmd([
            "samtools", "view", "-hb", sam_out, "--threads", str(NUM_THREADS),
            "-o", bam_out
        ])

        sorted_bam_out = os.path.join(BWA_DIR, "aligned.sorted.bam")
        yield from stream_cmd([
            "samtools", "sort", bam_out, "--threads", str(NUM_THREADS),
            "-o", sorted_bam_out
        ])
        yield from stream_cmd([
            "samtools", "index", sorted_bam_out, "--threads", str(NUM_THREADS)
        ])

        stat_out = os.path.join(BWA_DIR, "aligned.stat")
        yield "Generating flagstat…\n"
        with open(stat_out, "w") as out:
            p = subprocess.Popen(
                ["samtools", "flagstat", sorted_bam_out, "--threads", "1"],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, bufsize=1
            )
            for line in p.stdout:
                out.write(line)
                yield line
            p.wait()
            if p.returncode != 0:
                yield f"\n[ERROR] samtools flagstat exited with {p.returncode}\n"

        yield "✅ Alignment complete!\n"
        yield f"Read mapping complete with {genome}!\n"

    return Response(gen(), mimetype="text/plain")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
