from flask import Flask, request, jsonify, stream_with_context, Response
import os, subprocess
import threading

app = Flask(__name__)
NUM_THREADS = threading.active_count()

@app.route('/')
def index():
    return jsonify(message="Hello from Flask!")

def stream_cmd(cmd, cwd=None):
    """Run a command and yield its stdout+stderr lines in real time."""
    p = subprocess.Popen(
        cmd,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    for line in p.stdout:
        yield line
    p.wait()
    if p.returncode != 0:
        # Let the client know something failed
        yield f"\n[ERROR] {cmd} exited with {p.returncode}\n"

@app.route('/upload_r1_r2', methods=['POST'])
def upload_r1_r2():
    """
    curl -X POST http://localhost:5000/upload_r1_r2 \
      -F "R1=@/path/to/local/R1.fastq.gz" \
      -F "R2=@/path/to/local/R2.fastq.gz"
    """

    UPLOAD_DIR = "rawdata"
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    if 'R1' not in request.files or 'R2' not in request.files:
        return jsonify(error="Please upload both R1 and R2 files"), 400

    r1_file = request.files['R1']
    r2_file = request.files['R2']

    r1_path = os.path.join(UPLOAD_DIR, "R1.fastq.gz")
    r2_path = os.path.join(UPLOAD_DIR, "R2.fastq.gz")

    r1_file.save(r1_path)
    r2_file.save(r2_path)

    return jsonify(message="Upload successful")

@app.route('/qc_and_trimming', methods=['POST'])
def qc_and_trimming():
    """
    curl -X POST http://localhost:5000/qc_and_trimming
    """
    @stream_with_context
    def gen():
        RAW_DIR = "rawdata"
        CUT_DIR = "cutPrimer"
        FASTQC_BEFORE_OUT = "fastqc/beforeCutAdapt"
        FASTQC_AFTER_OUT  = "fastqc/afterCutAdapt"

        os.makedirs(FASTQC_BEFORE_OUT, exist_ok=True)
        os.makedirs(FASTQC_AFTER_OUT, exist_ok=True)
        os.makedirs(CUT_DIR, exist_ok=True)

        # fixed input file names
        R1_FILE = os.path.join(RAW_DIR, "R1.fastq.gz")
        R2_FILE = os.path.join(RAW_DIR, "R2.fastq.gz")

        # primer sequences
        r1_seq = "ATCCCTCAGACCCTTTTAGTCAGTGTGGAAAATCTC"
        r2_seq = "GACTGCGTATCAGT"

        # cutadapt parameters
        r1_error_rate = 0.1
        r1_trim_leading_trailing = 0
        r1_anchored = False
        r1_min_overlap = 0
        r1_pair_filter = "both"
        r1_minimum_length_of_read = 30

        r2_error_rate = 0.1
        r2_trim_leading_trailing = 0
        r2_anchored = False
        r2_min_overlap = 10
        r2_pair_filter = "both"
        r2_minimum_length_of_read = 30

        run_fastp = True

        # QC before trimming
        yield "Starting QC + trimming…\n"
        # stream fastqc output as example
        yield from stream_cmd(["fastqc", "-o", FASTQC_BEFORE_OUT, R1_FILE])
        yield "\nDone with R1 fastqc\n"

        yield "Starting QC + trimming…\n"
        # stream fastqc output as example
        yield from stream_cmd(["fastqc", "-o", FASTQC_BEFORE_OUT, R2_FILE])
        yield "\nDone with R2 fastqc\n"

        # optional fastp preprocessing
        if run_fastp:
            tmp_r1 = os.path.join(RAW_DIR, "R1.fastp.fastq.gz")
            tmp_r2 = os.path.join(RAW_DIR, "R2.fastp.fastq.gz")

            yield "\nRunning fastp…\n"
            yield from stream_cmd([
                "fastp",
                "-i", R1_FILE,
                "-I", R2_FILE,
                "-o", tmp_r1,
                "-O", tmp_r2
            ])

            # Replace originals with cleaned versions
            os.replace(tmp_r1, R1_FILE)
            os.replace(tmp_r2, R2_FILE) #TODO: WE SHOULDNT OVERWRITE THE R1 AND R2!!
            yield "fastp complete, originals replaced\n"

        # cutadapt step 1
        tmp1 = os.path.join(CUT_DIR, "step1_R1.fastq.gz")
        tmp2 = os.path.join(CUT_DIR, "step1_R2.fastq.gz")
        yield "\ncutadapt step 1…\n"
        yield from stream_cmd([
            "cutadapt",
            "-e", str(r1_error_rate),
            "--cut", str(r1_trim_leading_trailing),
            "-g", f"{'^' if r1_anchored else ''}{r1_seq};min_overlap={r1_min_overlap}",
            "--pair-filter", r1_pair_filter,
            "-m", str(r1_minimum_length_of_read),
            "-j", str(NUM_THREADS),
            "-o", tmp1,
            "-p", tmp2,
            R1_FILE,
            R2_FILE
        ])

        # cutadapt step 2
        out1 = os.path.join(CUT_DIR, "R1.fastq.gz")
        out2 = os.path.join(CUT_DIR, "R2.fastq.gz")
        yield "\ncutadapt step 2…\n"
        yield from stream_cmd([
            "cutadapt",
            "-e", str(r2_error_rate),
            "--cut", str(r2_trim_leading_trailing),
            "-G", f"{'^' if r2_anchored else ''}{r2_seq};min_overlap={r2_min_overlap}",
            "--pair-filter", r2_pair_filter,
            "-m", str(r2_minimum_length_of_read),
            "-j", str(NUM_THREADS),
            "-o", out1,
            "-p", out2,
            tmp1,
            tmp2
        ])

        os.remove(tmp1)
        os.remove(tmp2)
        yield "cutadapt complete\n"

        #TODO: Run umitools (depends on metadata)

        # QC after trimming
        yield "\nFastQC after trimming…\n"
        yield from stream_cmd(["fastqc", "-o", FASTQC_AFTER_OUT, out1])
        yield from stream_cmd(["fastqc", "-o", FASTQC_AFTER_OUT, out2])

        # Readlen analysis
        yield "\nRunning readlen analysis…\n"
        yield from stream_cmd(["Rscript", "readlen_analysis.R", out1, out2])

        #return the htmls or before and after fastqc and fastp
        yield "\n✅ QC and trimming complete!\n"

    return Response(gen(), mimetype="text/plain")

@app.route('/upload_ref_genome', methods=['POST'])
def upload_ref_genome():
    """
    curl -X POST http://localhost:5000/upload_ref_genome \
      -F "REF=@/path/to/local/reference_genome.tar.gz" \
      -F "NAME=test"
    """
    UPLOAD_DIR = "reference"
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    if 'REF' not in request.files:
        return jsonify(error="Please upload the reference genome"), 400
    if 'NAME' not in request.form:
        return jsonify(error="Please provide a NAME field"), 400

    ref_file = request.files['REF']
    ref_name = request.form['NAME']

    tar_path = os.path.join(UPLOAD_DIR, f"{ref_name}.fa.tar.gz")
    ref_file.save(tar_path)

    subprocess.run(["tar", "-xzf", tar_path, "-C", UPLOAD_DIR], check=True)

    return jsonify(message=f"Upload successful: {ref_name}")

@app.route('/read_mapping', methods=['POST'])
def read_mapping():
    """
    curl -X POST http://localhost:5000/read_mapping
    """
    @stream_with_context
    def gen():
        genome = "GRCh38.p14"
        tar_url = "https://nc.liam-w.com/s/abXeB3WtcWdm63f/download?path=%2F&files=GRCh38.p14.tar.gz"

        GENOME_DIR = "reference"
        CUT_DIR = "cutPrimer"
        R1_FILE = os.path.join(CUT_DIR, "R1.fastq.gz")
        R2_FILE = os.path.join(CUT_DIR, "R2.fastq.gz")
        BWA_DIR = "bwa"

        os.makedirs(GENOME_DIR, exist_ok=True)
        os.makedirs(BWA_DIR, exist_ok=True)

        idx_fa = os.path.join(GENOME_DIR, f"{genome}.fa")

        if not os.path.isfile(idx_fa + ".bwt.2bit.64"):
            yield f"📥 Downloading {genome} BWA index from nc…\n"
            tar_path = os.path.join(GENOME_DIR, f"{genome}.tar.gz")
            # download tar.gz
            yield from stream_cmd(["wget", tar_url, "-O", tar_path])
            # extract into GENOME_DIR
            yield from stream_cmd(["tar", "-xzf", tar_path, "-C", GENOME_DIR])
            yield "Download & extraction complete\n"

        yield f"🧬 Aligning reads using {genome}…\n"

        sam_out = os.path.join(BWA_DIR, "aligned.sam")
        yield from stream_cmd([
            "bwa-mem2", "mem",
            "-t", str(NUM_THREADS),
            idx_fa, R1_FILE, R2_FILE,
            "-o", sam_out
        ])

        bam_out = os.path.join(BWA_DIR, "aligned.bam")
        yield from stream_cmd([
            "samtools", "view",
            "-hb", sam_out,
            "--threads", str(NUM_THREADS),
            "-o", bam_out
        ])

        sorted_bam_out = os.path.join(BWA_DIR, "aligned.sorted.bam")
        yield from stream_cmd([
            "samtools", "sort",
            bam_out,
            "--threads", str(NUM_THREADS),
            "-o", sorted_bam_out
        ])
        yield from stream_cmd([
            "samtools", "index",
            sorted_bam_out,
            "--threads", str(NUM_THREADS)
        ])

        stat_out = os.path.join(BWA_DIR, "aligned.stat")
        yield "Generating flagstat…\n"
        with open(stat_out, "w") as out:
            p = subprocess.Popen(
                ["samtools", "flagstat", "bwa/aligned.sorted.bam", "--threads", "1"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
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
