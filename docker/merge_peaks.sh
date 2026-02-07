#!/bin/bash
# Peak merge pipeline extracted from site_analysis
# Usage: ./merge_peaks.sh BED_FILE OUT_PREFIX DEPTH BAM2BED_DIR PEAK_MERGE_OUTPUT

BED_FILE="$1"
OUT_PREFIX="$2"
DEPTH="$3"
BAM2BED_DIR="$4"
PEAK_MERGE="$5"

# Validate inputs
if [ $# -ne 5 ]; then
    echo "Usage: $0 BED_FILE OUT_PREFIX DEPTH BAM2BED_DIR PEAK_MERGE_OUTPUT"
    exit 1
fi

# Complex 8-stage peak merge pipeline
awk -F "\t" '{if($6=="+"){print $1"\t"$2"\t"$6} else {print $1"\t"$3"\t"$6}}' "$BED_FILE" |
grep -v vector | sort | uniq -c |
awk '{print $2"\t"$3"\t"$3+1"\t.\t"$1"\t"$4}' |
sort -k1,1 -k2,2n |
bedtools merge -c 5,6 -s -o sum,distinct -d "$DEPTH" -i - |
awk '{print $1"\t"$2"\t"$3"\t.\t"$4"\t"$5}' |
grep -v vector |
bedtools intersect -b <(grep -v vector "$BAM2BED_DIR/$OUT_PREFIX.bed" | awk '{if($6=="+"){print $1"\t"$2"\t"$2+1"\t.\t.\t"$6} else {print $1"\t"$3"\t"$3+1"\t.\t.\t"$6}}') -c -s -a - |
awk -v prefix="$OUT_PREFIX" '{print $1"\t"$2"\t"$3"\t"prefix"\t"$5"\t"$6"\t"$7}' > "$PEAK_MERGE"