from flask import Flask, request, jsonify, stream_with_context, Response
import os, subprocess, multiprocessing
import json

app = Flask(__name__)

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

def safe_stream(generator_func, endpoint_name):
    """Wrap a generator to ensure consistent error handling and final result reporting."""
    @stream_with_context
    def wrapper():
        result = {"endpoint": endpoint_name, "success": True, "error": None}
        try:
            yield from generator_func(result)
        except Exception as e:
            result["success"] = False
            result["error"] = str(e)
            yield "[TRACEBACK]\n" + "".join(traceback.format_exception(*sys.exc_info())) + "\n"
        finally:
            yield f"[RESULT] {json.dumps(result)}\n"
    return wrapper()

def stream_cmd(cmd, result, cwd=None):
    yield f"[INFO] Running: {' '.join(cmd)}\n"
    p = subprocess.Popen(
        cmd, cwd=cwd,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, bufsize=1
    )
    for line in p.stdout:
        yield f"[LOG] {line}"
    p.wait()

    if p.returncode == 0:
        yield f"[DONE] {cmd[0]} finished successfully\n"
        return True
    else:
        msg = f"{cmd[0]} exited with code {p.returncode}"
        result["success"] = False
        result["error"] = msg
        return False

@app.route('/upload_r1_r2', methods=['POST'])
def upload_r1_r2():
    """
    curl -N -X POST http://localhost:5000/upload_r1_r2 \
      -F "R1=@/home/liam-w/qsLAM_PCR_AIO/docker/rawdata/R1.fastq.gz" \
      -F "R2=@/home/liam-w/qsLAM_PCR_AIO/docker/rawdata/R2.fastq.gz"
    """
    def gen(result):
        os.makedirs(RAW_DIR, exist_ok=True)

        if 'R1' not in request.files or 'R2' not in request.files:
            msg = "Please upload both R1 and R2 files"
            result["success"] = False
            result["error"] = msg
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

    return Response(safe_stream(gen, "upload_r1_r2"), mimetype="text/plain")

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

    def gen(result):
        if stage == "before":
            outdir = FASTQC_BEFORE_OUT
            r1, r2 = R1_FILE, R2_FILE
        elif stage == "after":
            outdir = FASTQC_AFTER_OUT
            r1 = os.path.join(CUT_DIR, "R1.fastq.gz")
            r2 = os.path.join(CUT_DIR, "R2.fastq.gz")
        else:
            msg = f"Unknown stage: {stage}"
            result["success"] = False
            result["error"] = msg
            return

        os.makedirs(outdir, exist_ok=True)
        yield f"[INFO] Running FastQC ({stage})…\n"
        if not (yield from stream_cmd(["fastqc", "-o", outdir, r1], result)):
            return
        if not (yield from stream_cmd(["fastqc", "-o", outdir, r2], result)):
            return
        yield f"✅ QC ({stage}) complete\n"

    return Response(safe_stream(gen, "qc"), mimetype="text/plain")

@app.route('/umi', methods=['GET'])
def umi():
    """
    curl http://localhost:5000/umi
    """
    def gen(result):
        result["success"] = False
        result["error"] = "UMI step not implemented yet"
        return

    return Response(safe_stream(gen, "umi"), mimetype="text/plain")

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

    def gen(result):
        os.makedirs(CUT_DIR, exist_ok=True)

        r1_seq = params.get("r1_seq")
        r2_seq = params.get("r2_seq")

        if not r1_seq or not r2_seq:
            result["success"] = False
            result["error"] = "Missing r1_seq or r2_seq"
            return

        tmp1 = os.path.join(CUT_DIR, "step1_R1.fastq.gz")
        tmp2 = os.path.join(CUT_DIR, "step1_R2.fastq.gz")
        out1 = os.path.join(CUT_DIR, "R1.fastq.gz")
        out2 = os.path.join(CUT_DIR, "R2.fastq.gz")

        yield "[INFO] Cutadapt step 1…\n"
        if not (yield from stream_cmd([
            "cutadapt",
            "-e", str(params.get("r1_error_rate", 0.1)),
            "--cut", str(params.get("r1_trim_leading_trailing", 0)),
            "-g", f"{'^' if params.get('r1_anchored', False) else ''}{r1_seq};min_overlap={params.get('r1_min_overlap', 0)}",
            "--pair-filter", params.get("r1_pair_filter", "both"),
            "-m", str(params.get("r1_minimum_length_of_read", 30)),
            "-j", str(NUM_THREADS),
            "-o", tmp1,
            "-p", tmp2,
            R1_FILE,
            R2_FILE
        ], result)):
            return
        yield "[INFO] Cutadapt step 2…\n"
        if not (yield from stream_cmd([
            "cutadapt",
            "-e", str(params.get("r2_error_rate", 0.1)),
            "--cut", str(params.get("r2_trim_leading_trailing", 0)),
            "-G", f"{'^' if params.get('r2_anchored', False) else ''}{r2_seq};min_overlap={params.get('r2_min_overlap', 10)}",
            "--pair-filter", params.get("r2_pair_filter", "both"),
            "-m", str(params.get("r2_minimum_length_of_read", 30)),
            "-j", str(NUM_THREADS),
            "-o", out1,
            "-p", out2,
            tmp1,
            tmp2
        ], result)):
            return

        os.remove(tmp1)
        os.remove(tmp2)
        yield "✅ Cutadapt complete\n"

    return Response(safe_stream(gen, "cutadapt"), mimetype="text/plain")

@app.route('/fastp', methods=['GET'])
def fastp():
    """
    curl http://localhost:5000/fastp
    """
    def gen(result):
        tmp_r1 = os.path.join(RAW_DIR, "R1.fastp.fastq.gz")
        tmp_r2 = os.path.join(RAW_DIR, "R2.fastp.fastq.gz")

        yield "[INFO] Running fastp…\n"
        if not (yield from stream_cmd([
            "fastp",
            "-i", R1_FILE,
            "-I", R2_FILE,
            "-o", tmp_r1,
            "-O", tmp_r2
        ], result)):
            return
        yield f"[DONE] fastp complete → {tmp_r1}, {tmp_r2}\n"

    return Response(safe_stream(gen, "fastp"), mimetype="text/plain")

@app.route('/readlen', methods=['GET'])
def readlen():
    """
    curl http://localhost:5000/readlen
    """
    def gen(result):
        r1 = os.path.join(CUT_DIR, "R1.fastq.gz")
        r2 = os.path.join(CUT_DIR, "R2.fastq.gz")

        yield "[INFO] Running readlen analysis…\n"
        if not (yield from stream_cmd(["Rscript", "readlen_analysis.R", r1, r2], result)):
            return

        yield "✅ Readlen analysis complete\n"

    return Response(safe_stream(gen, "readlen"), mimetype="text/plain")

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
    curl -N -X POST http://localhost:5000/upload_ref_genome \
      -F "REF=@/home/liam-w/Downloads/mm10_cdna.tar.gz" \
      -F "NAME=mm10_cdna"
    """
    def gen(result):
        os.makedirs(REFERENCE, exist_ok=True)

        if 'REF' not in request.files:
            result["success"] = False
            result["error"] = "Please upload the reference genome (field: REF)"
            return
        if 'NAME' not in request.form:
            result["success"] = False
            result["error"] = "Please provide a NAME field"
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
        if not (yield from stream_cmd(["tar", "-xzf", tar_path, "-C", REFERENCE], result)):
            return
        os.remove(tar_path)
        yield "[DONE] Extraction complete\n"

        # Check for missing BWA-MEM2 index files
        missing = [s for s in required_suffixes if not os.path.isfile(idx_fa + s)]
        if missing:
            result["success"] = False
            result["error"] = f"Missing BWA-MEM2 index files: {', '.join(missing)}"
        else:
            yield f"[INFO] All BWA-MEM2 index files present for {ref_name}\n"

        yield f"✅ Reference genome uploaded and extracted: {ref_name}\n"

    return Response(safe_stream(gen, "upload_ref_genome"), mimetype="text/plain")

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
    or if reference already exists on the server, tar_url can be omitted:
    curl -N -X POST http://localhost:5000/read_mapping \
      -H "Content-Type: application/json" \
      -d '{
        "genome": "GRCh38.p14"
      }'
    """
    params = request.get_json(force=True)
    genome = params.get("genome")
    tar_url = params.get("tar_url")

    def gen(result):
        os.makedirs(REFERENCE, exist_ok=True)
        os.makedirs(BWA_DIR, exist_ok=True)

        idx_fa = os.path.join(REFERENCE, f"{genome}.fa")
        CUT_R1_FILE = os.path.join(CUT_DIR, "R1.fastq.gz")
        CUT_R2_FILE = os.path.join(CUT_DIR, "R2.fastq.gz")

        # Check if all bwa-mem2 index files exist
        if not has_bwa_mem2_index(idx_fa):
            if not tar_url:
                result["success"] = False
                result["error"] = f"Reference {genome} not found and no tar_url provided.\n"
                return
            yield f"📥 Downloading {genome} BWA-MEM2 index from {tar_url}…\n"
            tar_path = os.path.join(REFERENCE, f"{genome}.tar.gz")
            if not (yield from stream_cmd(["wget", tar_url, "-O", tar_path], result)):
                return
            if not (yield from stream_cmd(["tar", "-xzf", tar_path, "-C", REFERENCE], result)):
                return
            os.remove(tar_path)
            yield "Download & extraction complete\n"

        yield f"🧬 Aligning reads using {genome}…\n"
        sam_out = os.path.join(BWA_DIR, "aligned.sam")
        if not (yield from stream_cmd([
            "bwa-mem2", "mem", "-t", str(NUM_THREADS),
            idx_fa, CUT_R1_FILE, CUT_R2_FILE, "-o", sam_out
        ], result)):
            return

        bam_out = os.path.join(BWA_DIR, "aligned.bam")
        if not (yield from stream_cmd([
            "samtools", "view", "-hb", sam_out, "--threads", str(NUM_THREADS),
            "-o", bam_out
        ], result)):
            return

        sorted_bam_out = os.path.join(BWA_DIR, "aligned.sorted.bam")
        if not (yield from stream_cmd([
            "samtools", "sort", bam_out, "--threads", str(NUM_THREADS),
            "-o", sorted_bam_out
        ], result)):
            return

        if not (yield from stream_cmd([
            "samtools", "index", sorted_bam_out, "--threads", str(NUM_THREADS)
        ], result)):
            return

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
                result["success"] = False
                result["error"] = f"samtools flagstat exited with {p.returncode}"
                return

        yield "✅ Alignment complete!\n"
        yield f"Read mapping complete with {genome}!\n"

    return Response(safe_stream(gen, "read_mapping"), mimetype="text/plain")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
