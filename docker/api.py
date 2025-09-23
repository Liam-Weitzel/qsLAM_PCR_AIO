from flask import Flask, request, jsonify
import os, subprocess
import threading

app = Flask(__name__)
NUM_THREADS = threading.active_count()

@app.route('/')
def index():
    return jsonify(message="Hello from Flask!")

@app.route('/qc_and_trimming')
def qc_and_trimming():
    #TODO: Allow user to upload raw data
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
    subprocess.run(["fastqc", "-o", FASTQC_BEFORE_OUT, R1_FILE])
    subprocess.run(["fastqc", "-o", FASTQC_BEFORE_OUT, R2_FILE])

    # optional fastp preprocessing
    if run_fastp:
        tmp_r1 = os.path.join(RAW_DIR, "R1.fastp.fastq.gz")
        tmp_r2 = os.path.join(RAW_DIR, "R2.fastp.fastq.gz")

        subprocess.run([
            "fastp",
            "-i", R1_FILE,
            "-I", R2_FILE,
            "-o", tmp_r1,
            "-O", tmp_r2
        ], check=True)

        # Replace originals with cleaned versions
        os.replace(tmp_r1, R1_FILE)
        os.replace(tmp_r2, R2_FILE)

    # cutadapt step 1
    tmp1 = os.path.join(CUT_DIR, "step1_R1.fastq.gz")
    tmp2 = os.path.join(CUT_DIR, "step1_R2.fastq.gz")
    subprocess.run([
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
    ], check=True)

    # cutadapt step 2
    out1 = os.path.join(CUT_DIR, "R1.fastq.gz")
    out2 = os.path.join(CUT_DIR, "R2.fastq.gz")
    subprocess.run([
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
    ], check=True)

    os.remove(tmp1)
    os.remove(tmp2)

    #TODO: Run umitools (depends on metadata)

    # QC after trimming
    subprocess.run(["fastqc", "-o", FASTQC_AFTER_OUT, out1])
    subprocess.run(["fastqc", "-o", FASTQC_AFTER_OUT, out2])

    # Readlen analysis
    subprocess.run(["Rscript", "readlen_analysis.R", out1, out2])

    #return the htmls or before and after fastqc and fastp

    return jsonify(message="QC and trimming complete!")

@app.route('/read_mapping')
def read_mapping():
    #TODO: Allow user to uplaod ref genome not in refgenomes.databio
    genome = "baa91c8f6e2780cfd8fd1040ff37f51c379947a2a4820d6c"

    GENOME_DIR = "reference"
    CUT_DIR = "cutPrimer"
    R1_FILE = os.path.join(CUT_DIR, "R1.fastq.gz")
    R2_FILE = os.path.join(CUT_DIR, "R2.fastq.gz")
    BWA_DIR = "bwa"

    os.makedirs(GENOME_DIR, exist_ok=True)
    os.makedirs(BWA_DIR, exist_ok=True)

    tar_url = f"http://refgenomes.databio.org/v3/assets/archive/{genome}/bwa_index"
    idx_fa = os.path.join(GENOME_DIR, f"{genome}.fa")

    if not os.path.isfile(idx_fa + ".bwt"):
        print(f"📥 Downloading {genome} BWA index from refgenomes…")
        tar_path = os.path.join(GENOME_DIR, f"{genome}_bwa_index.tar.gz")
        # download tar.gz
        subprocess.run(["wget", "-O", tar_path, tar_url], check=True)
        # extract into GENOME_DIR
        subprocess.run(["tar", "-xzf", tar_path, "-C", GENOME_DIR], check=True)
        os.remove(tar_path)
        # move files out of nested default/ folder and remove it
        nested_dir = os.path.join(GENOME_DIR, "default")
        for f in os.listdir(nested_dir):
            src = os.path.join(nested_dir, f)
            dst = os.path.join(GENOME_DIR, f)
            subprocess.run(["mv", src, dst], check=True)

        # then remove the now-empty directories
        os.rmdir(nested_dir)

    # === Alignment ===

    print(f"🧬 Aligning reads using {genome}…")

    sam_out = os.path.join(BWA_DIR, "aligned.sam")
    subprocess.run(
        ["bwa-mem2", "mem", "-t", str(NUM_THREADS), idx_fa, R1_FILE, R2_FILE, "-o", sam_out],
        check=True
    )

    bam_out = os.path.join(BWA_DIR, "aligned.bam")
    subprocess.run(["samtools", "view", "-hb", sam_out, "-o", bam_out], check=True)

    sorted_bam_out = os.path.join(BWA_DIR, "aligned.sorted.bam")
    subprocess.run(["samtools", "sort", bam_out, "-o", sorted_bam_out], check=True)
    subprocess.run(["samtools", "index", sorted_bam_out], check=True)

    stat_out = os.path.join(BWA_DIR, "aligned.stat")
    subprocess.run(["samtools", "flagstat", sorted_bam_out, "-o", stat_out], check=True)

    print("✅ Alignment complete!")
    return jsonify(message=f"Read mapping complete with {genome}!")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
