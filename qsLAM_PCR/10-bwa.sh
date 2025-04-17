#!/bin/bash
#
#BSUB -P insertionSite         # project code
#BSUB -J bwa      # job name
#BSUB -W 10:00                # wall-clock time (hrs:mins)
#BSUB -n 4	# number of cpu
#BSUB -R "rusage[mem=8000]"     # memory to reserve, in MB
#BSUB -e errors.%J     # error file name in which %J is replaced by the job ID
#BSUB -o output.%J     # output file name in which %J is replaced by the job ID

# module load bwa
# module load samtools/1.10
# idx=/research/projects/yu3grp/IO_JY/yu3grp/LVXSCID/patients_scATACseq/bwa_index/hg19/hg19idx

# Parse command line arguments
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
mkdir -p ${GENOME_DIR}

if $INDEX_FROM_SCRATCH; then
    echo "Using from-scratch indexing approach..."
    if [ ! -f ${GENOME_DIR}/hg19.fa ]; then
        echo "Downloading hg19 reference..."
        wget -P ${GENOME_DIR} https://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.fa.gz
        gunzip ${GENOME_DIR}/hg19.fa.gz
    fi

    if [ ! -f ${GENOME_DIR}/hg19.fa.bwt ]; then
        echo "Creating BWA index..."
        bwa index ${GENOME_DIR}/hg19.fa
    fi
    idx="${GENOME_DIR}/hg19.fa"
else
    echo "Using pre-indexed approach..."
    if [ ! -f ${GENOME_DIR}/hg19.p13.plusMT.no_alt_analysis_set.fa.bwt ]; then
        echo "Downloading pre-indexed hg19..."
        wget http://hgdownload.cse.ucsc.edu/goldenpath/hg19/bigZips/analysisSet/hg19.p13.plusMT.no_alt_analysis_set.bwa_index.tar.gz
        tar -xzf hg19.p13.plusMT.no_alt_analysis_set.bwa_index.tar.gz -C ${GENOME_DIR}
        mv ${GENOME_DIR}/hg19.p13.plusMT.no_alt_analysis_set/* ${GENOME_DIR}/
        rmdir ${GENOME_DIR}/hg19.p13.plusMT.no_alt_analysis_set
        rm hg19.p13.plusMT.no_alt_analysis_set.bwa_index.tar.gz
    fi
    idx="${GENOME_DIR}/hg19.p13.plusMT.no_alt_analysis_set.fa"
fi

mkdir -p bwa
for fq_R1 in `ls newFastq/ | grep -P "fastq$" | grep R1`
do
    fq_R2=`echo $fq_R1| sed 's/R1/R2/'`
    bwa_out=`echo $fq_R1| sed 's/fastq/bam/' `
    if [ ! -e bwa/$bwa_out ]; then 
        bwa mem -t 4 $idx newFastq/$fq_R1 newFastq/$fq_R2 | samtools view -hbS - > bwa/$bwa_out
        samtools sort bwa/$bwa_out -o bwa/${bwa_out%.bam}.sorted.bam
        samtools index bwa/${bwa_out%.bam}.sorted.bam
        samtools flagstat bwa/${bwa_out%.bam}.sorted.bam > bwa/${bwa_out%.bam}.stat
    fi
done
