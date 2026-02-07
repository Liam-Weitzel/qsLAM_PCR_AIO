#!/bin/bash
# BED file deduplication pipeline extracted from site_analysis
# Usage: ./deduplicate_bed.sh INPUT_BED OUTPUT_BED

INPUT_BED="$1"
OUTPUT_BED="$2"

# Validate inputs
if [ $# -ne 2 ]; then
    echo "Usage: $0 INPUT_BED OUTPUT_BED"
    exit 1
fi

# Deduplication pipeline: extract columns, sort unique, reformat
cut -f 1,2,3,6 "$INPUT_BED" | sort -u | \
awk '{print $1"\t"$2"\t"$3"\t.\t.\t"$4}' > "$OUTPUT_BED"