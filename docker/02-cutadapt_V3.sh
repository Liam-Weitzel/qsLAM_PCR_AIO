#!/bin/bash
#BSUB -P insertionSite
#BSUB -J cutPrimer
#BSUB -W 40:00
#BSUB -R "rusage[mem=8000]"
#BSUB -e errors.%J.hybrid
#BSUB -o output.%J.hybrid

mkdir -p cutPrimer

LTR_PRIMER="ATCCCTCAGACCCTTTTAGTCAGTGTGGAAAATCTC"  # R1
ADAPTER="GACTGCGTATCAGT"                           # R2

for r1 in rawdata/*R1*.fastq.gz; do
    r2="${r1/R1/R2}"
    
    if [ ! -f "$r2" ]; then
        echo "❌ Missing R2 file for $r1"
        continue
    fi

    sample_name=$(basename "$r1" | sed 's/_R1.*.fastq.gz//')
    tmp1="cutPrimer/${sample_name}_step1_R1.fastq.gz"
    tmp2="cutPrimer/${sample_name}_step1_R2.fastq.gz"
    out1="cutPrimer/${sample_name}_R1.retain.fastq.gz"
    out2="cutPrimer/${sample_name}_R2.retain.fastq.gz"
    info1="cutPrimer/${sample_name}_R1.adapter_info.txt"
    info2="cutPrimer/${sample_name}_R2.adapter_info.txt"

    if [ -e "$out1" ] && [ -e "$out2" ]; then
        echo "✅ Trimmed files for $sample_name already exist. Skipping."
        continue
    fi

    echo "🔍 Step 1: Trimming LTR from R1 at 40% error"
    cutadapt \
        -e 0.4 \
        --cut 9 \
        -g "^${LTR_PRIMER}" \
        --pair-filter=both \
        -m 20 \
        -o "$tmp1" -p "$tmp2" \
        "$r1" "$r2"

    echo "🔍 Step 2: Trimming ADAPTER from R2 at 10% error"
    cutadapt \
        -e 0.1 \
        -G "${ADAPTER};min_overlap=10" \
        --pair-filter=both \
        -m 20 \
        --info-file="$info2" \
        -o "$out1" -p "$out2" \
        "$tmp1" "$tmp2"

    rm "$tmp1" "$tmp2"
done

