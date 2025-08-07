#!/bin/bash
#
#BSUB -P insertionSite
#BSUB -J makeNewFastQ
#BSUB -W 40:00
#BSUB -R "rusage[mem=8000]"
#BSUB -e errors.%J.hybrid
#BSUB -o output.%J.hybrid

mkdir -p newFastq

for fq_R1 in cutPrimer/*R1*.fastq.gz; do
    fq_R2="${fq_R1/R1/R2}"
    fq_R1_name=$(basename "$fq_R1")
    fq_R2_name=$(basename "$fq_R2")

    if [ -e newFastq/"$fq_R1_name" ] && [ -e newFastq/"$fq_R2_name" ]; then
        echo "✅ Output for $fq_R1_name already exists. Skipping."
        continue
    fi

    echo "🔄 Processing $fq_R1_name..."

    # Merge read pairs side by side
    paste <(zcat "$fq_R1" | paste - - - - | sed 's/^.//') \
          <(zcat "$fq_R2" | paste - - - - | sed 's/^.//') > temp.fastq

    total_reads=$(wc -l < temp.fastq)
    total_pairs=$((total_reads))

    # Filter read pairs where both R1 and R2 are ≥30 bp
    awk -F "\t" 'length($4) >= 30 && length($8) >= 30' temp.fastq > temp_filtered.tsv
    kept_pairs=$(wc -l < temp_filtered.tsv)
    discarded_pairs=$((total_pairs - kept_pairs))

    # Output summary
    echo "📊 Total read pairs:     $total_pairs"
    echo "✅ Passed filter (≥30bp): $kept_pairs"
    echo "❌ Discarded:             $discarded_pairs"

    # Write FASTQ output
    cut -f1-4 temp_filtered.tsv | sed 's/^/@/' | tr '\t' '\n' | gzip > newFastq/"$fq_R1_name"
    cut -f5-8 temp_filtered.tsv | sed 's/^/@/' | tr '\t' '\n' | gzip > newFastq/"$fq_R2_name"

    rm temp.fastq temp_filtered.tsv
done

