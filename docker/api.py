from flask import Flask, request, jsonify, stream_with_context, Response
import os, subprocess, multiprocessing
import json
import traceback
import sys

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
BAM2BED_DIR = "bam2bed"
BED2PEAK_DIR = "bed2peak"

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

def stream_cmd(cmd, result, cwd=None, cmd_is_shell=False):
    if isinstance(cmd, str) and not cmd_is_shell:
        cmd = cmd.split()
    yield f"[INFO] Running: {cmd if cmd_is_shell else ' '.join(cmd)}\n"
    p = subprocess.Popen(
        cmd, cwd=cwd,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, bufsize=1,
        shell=cmd_is_shell
    )
    for line in p.stdout:
        yield f"[LOG] {line}"
    p.wait()

    if p.returncode == 0:
        yield f"[DONE] {cmd[0] if not cmd_is_shell else cmd} finished successfully\n"
        return True
    else:
        msg = f"{cmd[0] if not cmd_is_shell else cmd} exited with code {p.returncode}"
        result["success"] = False
        result["error"] = msg
        return False

@app.route('/upload_r1_r2', methods=['POST'])
def upload_r1_r2():
    """
    curl -N -X POST http://127.0.0.1:32768/upload_r1_r2 \
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
    curl -N -X POST http://127.0.0.1:32768/qc \
      -H "Content-Type: application/json" \
      -d '{"stage": "before"}'
    or
    curl -N -X POST http://127.0.0.1:32768/qc \
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
    curl http://127.0.0.1:32768/umi
    """
    def gen(result):
        result["success"] = False
        result["error"] = "UMI step not implemented yet"
        return

    return Response(safe_stream(gen, "umi"), mimetype="text/plain")

@app.route('/cutadapt', methods=['POST'])
def cutadapt():
    """
    curl -N -X POST http://127.0.0.1:32768/cutadapt \
      -H "Content-Type: application/json" \
      -d '{
        "r1_seq": "ATCCCTCAGACCCTTTTAGTCAGTGTGGAAAATCTC",
        "r2_seq": "GACTGCGTATCAGT",
        "r1_error_rate": 0.3,
        "r1_trim_leading_trailing": 0,
        "r1_anchored": false,
        "r1_min_overlap": 5,
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
            "-e", str(params.get("r1_error_rate", 0.3)),
            "--cut", str(params.get("r1_trim_leading_trailing", 0)),
            "-g", f"{'^' if params.get('r1_anchored', False) else ''}{r1_seq};min_overlap={params.get('r1_min_overlap', 5)}",
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
    curl http://127.0.0.1:32768/fastp
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
    curl http://127.0.0.1:32768/readlen
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

@app.route('/read_mapping', methods=['POST'])
def read_mapping():
    """
    curl -N -X POST http://127.0.0.1:32768/read_mapping \
      -H "Content-Type: application/json" \
      -d '{
        "genome": "hg38",
        "tar_url": "https://nc.liam-w.com/s/abXeB3WtcWdm63f/download?path=%2F&files=hg38.tar.gz"
      }'
    or if reference already exists on the server, tar_url can be omitted:
    curl -N -X POST http://127.0.0.1:32768/read_mapping \
      -H "Content-Type: application/json" \
      -d '{
        "genome": "hg38"
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
        if not (yield from stream_cmd(
            f"samtools flagstat {sorted_bam_out} --threads {str(NUM_THREADS)} > {stat_out}",
            result,
            cmd_is_shell=True
        )):
            return

        with open(stat_out, "r") as f:
            for line in f:
                yield line

        yield "✅ Alignment complete!\n"

    return Response(safe_stream(gen, "read_mapping"), mimetype="text/plain")

@app.route('/site_analysis', methods=['POST'])
def site_analysis():
    """
    curl -N -X POST http://127.0.0.1:32768/site_analysis \
      -H "Content-Type: application/json" \
      -d '{
        "genome": "hg38",
        "promoter.left": "5000",
        "promoter.right": "2000",
        "enhancer.left": "50000"
      }'
    """
    params = request.get_json(force=True)
    genome = params.get("genome")
    promoter_left = params.get("promoter.left")
    promoter_right = params.get("promoter.right")
    enhancer_left = params.get("enhancer.left")

    def gen(result):
        os.makedirs(BAM2BED_DIR, exist_ok=True)

        for bam in os.listdir(BWA_DIR):
            if not bam.endswith(".bam"):
                continue

            out_prefix = os.path.splitext(bam)[0]
            yield f"[INFO] Processing {out_prefix}\n"

            rmdup_bed = os.path.join(BAM2BED_DIR, f"{out_prefix}.rmdup.bed")
            if os.path.exists(rmdup_bed):
                yield f"[SKIP] {rmdup_bed} already exists\n"
                continue

            bam_path = os.path.join(BWA_DIR, bam)
            header_sam = os.path.join(BAM2BED_DIR, f"{out_prefix}.header.sam")
            reads_sam  = os.path.join(BAM2BED_DIR, f"{out_prefix}.reads.sam")
            filtered_sam = os.path.join(BAM2BED_DIR, f"{out_prefix}.sam")
            bam_unsorted = os.path.join(BAM2BED_DIR, f"{out_prefix}.unsorted.bam")
            sorted_bam = os.path.join(BAM2BED_DIR, f"{out_prefix}.sorted.bam")
            temp_bedpe = os.path.join(BAM2BED_DIR, f"{out_prefix}.temp")
            bed_file = os.path.join(BAM2BED_DIR, f"{out_prefix}.bed")
            sam_temp = os.path.join(BAM2BED_DIR, f"{out_prefix}.sam.tmp")

            # 1. Extract header
            if not (yield from stream_cmd(["samtools", "view", "-H", bam_path, "-o", header_sam], result)):
                return

            # 2. Extract filtered reads
            if not (yield from stream_cmd(["samtools", "view", "-F", "4", bam_path, "-o", reads_sam], result)):
                return

            # 3. Filter reads (filter_reads.pl writes to filtered_sam)
            if not (yield from stream_cmd(["perl", "filter_reads.pl", reads_sam, filtered_sam], result)):
                return

            # 4. Combine header + filtered reads into final SAM (use temp file)
            combined_sam = os.path.join(BAM2BED_DIR, f"{out_prefix}.sam.tmp")
            if not (yield from stream_cmd(
                ["bash", "-c", f"cat {header_sam} {filtered_sam} > {combined_sam}"],
                result
            )):
                return

            # Replace filtered_sam with combined_sam
            filtered_sam = combined_sam

            # 5. Convert to BAM (unsorted)
            if not (yield from stream_cmd(["samtools", "view", "-hbS", filtered_sam, "-o", bam_unsorted], result)):
                return

            # 6. Sort BAM by name
            if not (yield from stream_cmd([
                    "samtools", "sort", "-n",
                    "-o", sorted_bam,
                    "-T", f"{BAM2BED_DIR}/{out_prefix}.tmp",
                    bam_unsorted
            ], result)):
                return

            # 7. Convert sorted BAM to BEDPE
            if not (yield from stream_cmd(["bash", "-c", f"bedtools bamtobed -i {sorted_bam} -bedpe -mate1 > {temp_bedpe}"], result)):
                return

            # 8. Convert BEDPE to BED
            if not (yield from stream_cmd(["perl", "bedpe_to_bed.pl", temp_bedpe, bed_file], result)):
                return

            # 9. Remove duplicates
            if not (yield from stream_cmd([
                "bash", "-c", f"cut -f 1,2,3,6 {bed_file} | sort -u | "
                               "awk '{print $1\"\\t\"$2\"\\t\"$3\"\\t.\\t.\\t\"$4}' "
                               f"> {rmdup_bed}"
            ], result)):
                return

            # Clean up temp files
            for f in [bam_unsorted, temp_bedpe, sorted_bam, sam_temp, header_sam, reads_sam]:
                if os.path.exists(f):
                    os.remove(f)

            yield f"✅ Site analysis complete for {out_prefix}\n"

        # === bed2peak analysis ===
        yield "[INFO] Starting bed2peak analysis…\n"
        rmdup_beds = [f for f in os.listdir(BAM2BED_DIR) if f.endswith("rmdup.bed")]
        os.makedirs(BED2PEAK_DIR, exist_ok=True)

        for d in range(11):
            for bed_file in rmdup_beds:
                out_prefix = bed_file.replace(".rmdup.bed", "")
                yield f"[INFO] bed2peak d={d}, sample={out_prefix}\n"

                # include depth in filenames
                peak_merge  = os.path.join(BED2PEAK_DIR, f"{out_prefix}.d{d}.peak.merge.txt")
                all_peaks   = os.path.join(BED2PEAK_DIR, f"{out_prefix}.d{d}.all_peaks.txt")
                peak_merge2 = os.path.join(BED2PEAK_DIR, f"{out_prefix}.d{d}.peak.merge.2.txt")
                peak_merge3 = os.path.join(BED2PEAK_DIR, f"{out_prefix}.d{d}.peak.merge.3.txt")
                peak_xlsx   = os.path.join(BED2PEAK_DIR, f"{out_prefix}.d{d}.peak.merge.xlsx")

                # Merge peaks
                cmd_merge = f"""
                  awk -F "\\t" '{{if($6=="+"){{print $1"\\t"$2"\\t"$6}} else {{print $1"\\t"$3"\\t"$6}}}}' {BAM2BED_DIR}/{bed_file} |
                  grep -v vector | sort | uniq -c |
                  awk '{{print $2"\\t"$3"\\t"$3+1"\\t.\\t"$1"\\t"$4}}' |
                  sort -k1,1 -k2,2n |
                  bedtools merge -c 5,6 -s -o sum,distinct -d {d} -i - |
                  awk '{{print $1"\\t"$2"\\t"$3"\\t.\\t"$4"\\t"$5}}' |
                  grep -v vector |
                  bedtools intersect -b <(grep -v vector {BAM2BED_DIR}/{out_prefix}.bed | awk '{{if($6=="+"){{print $1"\\t"$2"\\t"$2+1"\\t.\\t.\\t"$6}} else {{print $1"\\t"$3"\\t"$3+1"\\t.\\t.\\t"$6}}}}') -c -s -a - |
                  awk '{{print $1"\\t"$2"\\t"$3"\\t{out_prefix}\\t"$5"\\t"$6"\\t"$7}}' > {peak_merge}
                """
                if not (yield from stream_cmd(["bash", "-c", cmd_merge], result)):
                    return

                # All peaks
                cmd_all = f"""
                  awk -F "\\t" '{{if($6=="+"){{print $1"\\t"$2"\\t"$6}} else {{print $1"\\t"$3"\\t"$6}}}}' {BAM2BED_DIR}/{bed_file} |
                  grep -v vector | sort | uniq -c |
                  awk '{{print $2"\\t"$3"\\t"$3+1"\\t.\\t"$1"\\t"$4}}' |
                  sort -k1,1 -k2,2n |
                  grep -v vector |
                  bedtools intersect -b <(grep -v vector {BAM2BED_DIR}/{out_prefix}.bed | awk '{{if($6=="+"){{print $1"\\t"$2"\\t"$2+1"\\t.\\t.\\t"$6}} else {{print $1"\\t"$3"\\t"$3+1"\\t.\\t.\\t"$6}}}}') -c -s -a - |
                  awk '{{print $1"\\t"$2"\\t"$3"\\t{out_prefix}\\t"$5"\\t"$6"\\t"$7}}' > {all_peaks}
                """
                if not (yield from stream_cmd(["bash", "-c", cmd_all], result)):
                    return

                # Windowed intersection
                cmd_window = f"bedtools window -w {d} -a {peak_merge} -b known20sites.bed -sm -c > {peak_merge2}"
                if not (yield from stream_cmd(["bash", "-c", cmd_window], result)):
                    return

                # Step 1: Gene prediction
                if not (yield from stream_cmd(["Rscript", "peak_annotation_step1.R", peak_merge2, peak_merge3, genome, promoter_left, promoter_right, enhancer_left], result)):
                    return

                # Step 2: Excel export
                if not (yield from stream_cmd(["Rscript", "peak_annotation_step2.R", peak_merge3, peak_xlsx], result)):
                    return

        yield "✅ Peak annotation complete!\n"

    return Response(safe_stream(gen, "site_analysis"), mimetype="text/plain")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
