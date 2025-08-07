#!/bin/bash
#
#BSUB -P insertionSite         # project code
#BSUB -J bwa                   # job name
#BSUB -W 10:00                 # wall-clock time (hrs:mins)
#BSUB -n 4                     # number of CPU cores
#BSUB -R "rusage[mem=8000]"    # memory to reserve, in MB
#BSUB -e errors.%J             # error file name
#BSUB -o output.%J             # output file name

# module load bwa
# module load samtools/1.10

# Parse command-line arguments
INDEX_FROM_SCRATCH=false
while [[ $# -gt 0 ]]; do
    case $1 in
        -index)
            INDEX_FROM_SCRATCH=true
            shift
            ;;
        *)
            echo "Unknown parameter: $1"
            exit 1
            ;;
    esac
done

# Set up reference genome and index
GENOME_DIR="reference"
mkdir -p "${GENOME_DIR}"

if $INDEX_FROM_SCRATCH; then
    echo "🔧 Using from-scratch indexing..."
    if [ ! -f ${GENOME_DIR}/hg19.fa ]; then
        echo "📥 Downloading hg19 reference..."
        wget -P ${GENOME_DIR} https://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.fa.gz
        gunzip ${GENOME_DIR}/hg19.fa.gz
    fi

    if [ ! -f ${GENOME_DIR}/hg19.fa.bwt ]; then
        echo "🧬 Indexing hg19 with BWA..."
        bwa index ${GENOME_DIR}/hg19.fa
    fi

    idx="${GENOME_DIR}/hg19.fa"
else
    echo "📁 Using pre-indexed reference..."
    if [ ! -f ${GENOME_DIR}/hg19.p13.plusMT.no_alt_analysis_set.fa.bwt ]; then
        echo "📥 Downloading pre-indexed hg19 set..."
        wget http://hgdownload.cse.ucsc.edu/goldenpath/hg19/bigZips/analysisSet/hg19.p13.plusMT.no_alt_analysis_set.bwa_index.tar.gz
        tar -xzf hg19.p13.plusMT.no_alt_analysis_set.bwa_index.tar.gz -C ${GENOME_DIR}
        mv ${GENOME_DIR}/hg19.p13.plusMT.no_alt_analysis_set/* ${GENOME_DIR}/
        rmdir ${GENOME_DIR}/hg19.p13.plusMT.no_alt_analysis_set
        rm hg19.p13.plusMT.no_alt_analysis_set.bwa_index.tar.gz
    fi

    idx="${GENOME_DIR}/hg19.p13.plusMT.no_alt_analysis_set.fa"
fi

# Align reads
mkdir -p bwa
for fq_R1 in newFastq/*R1*.fastq.gz; do
    fq_R2="${fq_R1/R1/R2}"
    sample_name=$(basename "$fq_R1" | sed 's/_R1.*\.fastq\.gz//')
    bam_out="bwa/${sample_name}.bam"
    sorted_bam_out="bwa/${sample_name}.sorted.bam"
    stat_out="bwa/${sample_name}.stat"

    if [ -e "$stat_out" ]; then
        echo "✅ BAM for $sample_name already exists. Skipping."
        continue
    fi

    echo "🧬 Aligning $sample_name..."

    bwa mem -t 4 "$idx" "$fq_R1" "$fq_R2" | samtools view -hbS - > "$bam_out"
    samtools sort "$bam_out" -o "$sorted_bam_out"
    samtools index "$sorted_bam_out"
    samtools flagstat "$sorted_bam_out" > "$stat_out"
done
