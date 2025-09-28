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

@app.route('/qc_and_trimming')
def qc_and_trimming():
    @stream_with_context
    def gen():
        #TODO: Allow user to upload raw data
        # Allow user to provide download link for data
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
            os.replace(tmp_r2, R2_FILE)
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

@app.route('/read_mapping')
def read_mapping():
    @stream_with_context
    def gen():
        #TODO: Allow user to upload ref genome
        # Allow user to provide download link for ref genome
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
