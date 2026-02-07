#!/bin/bash
# site_analysis.sh - Complete site analysis pipeline wrapper
#
# Chains all 6 stages: BAM-to-BED conversion, deduplication, peak detection,
# peak merging, gene annotation, and Excel export.
#
# Usage: site_analysis.sh WORKSPACE_DIR SCRIPT_DIR GENOME PROMOTER_LEFT PROMOTER_RIGHT ENHANCER_LEFT
#
#   WORKSPACE_DIR   - Absolute path to the run workspace (runs/{run_id})
#   SCRIPT_DIR      - Absolute path to directory containing helper scripts
#   GENOME          - Genome name (GRCh38, GRCm39, etc.)
#   PROMOTER_LEFT   - Promoter left boundary (e.g., 5000)
#   PROMOTER_RIGHT  - Promoter right boundary (e.g., 2000)
#   ENHANCER_LEFT   - Enhancer left boundary (e.g., 50000)

set -euo pipefail

# --- Argument validation ---
if [ $# -ne 6 ]; then
    echo "Usage: $0 WORKSPACE_DIR SCRIPT_DIR GENOME PROMOTER_LEFT PROMOTER_RIGHT ENHANCER_LEFT"
    exit 1
fi

# --- Arguments ---
WORKSPACE_DIR="$1"
SCRIPT_DIR="$2"
GENOME="$3"
PROMOTER_LEFT="$4"
PROMOTER_RIGHT="$5"
ENHANCER_LEFT="$6"

# --- Derived paths ---
BAM2BED_DIR="${WORKSPACE_DIR}/bam2bed"
BED2PEAK_DIR="${WORKSPACE_DIR}/bed2peak"
BWA_DIR="${WORKSPACE_DIR}/bwa"
SORTED_BAM="${BWA_DIR}/aligned.sorted.bam"
OUT_PREFIX="aligned.sorted"
KNOWN_SITES="${SCRIPT_DIR}/known20sites.bed"

# --- Prerequisite validation ---
if [ ! -f "${SORTED_BAM}" ]; then
    echo "ERROR: Sorted BAM file not found: ${SORTED_BAM}"
    echo "Run read_mapping first."
    exit 1
fi

# === Cleanup: removing previous site_analysis outputs ===
echo "=== Cleanup: removing previous site_analysis outputs ==="
rm -rf "${BAM2BED_DIR:?}"/*
rm -rf "${BED2PEAK_DIR:?}"/*
mkdir -p "${BAM2BED_DIR}" "${BED2PEAK_DIR}"
echo "Cleanup complete"

# === Stage 1: BAM to BED conversion ===
echo "=== Stage 1: BAM to BED conversion ==="

# Intermediate file paths
HEADER_SAM="${BAM2BED_DIR}/${OUT_PREFIX}.header.sam"
READS_SAM="${BAM2BED_DIR}/${OUT_PREFIX}.reads.sam"
FILTERED_SAM="${BAM2BED_DIR}/${OUT_PREFIX}.filtered.sam"
COMBINED_SAM="${BAM2BED_DIR}/${OUT_PREFIX}.sam.tmp"
BAM_UNSORTED="${BAM2BED_DIR}/${OUT_PREFIX}.unsorted.bam"
NAMESORT_BAM="${BAM2BED_DIR}/${OUT_PREFIX}.namesort.bam"
TEMP_BEDPE="${BAM2BED_DIR}/${OUT_PREFIX}.temp"
BED_FILE="${BAM2BED_DIR}/${OUT_PREFIX}.bed"

# 1. Extract header
samtools view -H "${SORTED_BAM}" -o "${HEADER_SAM}"

# 2. Extract mapped reads (exclude unmapped flag 4)
samtools view -F 4 "${SORTED_BAM}" -o "${READS_SAM}"

# 3. Filter reads (remove clipped reads)
perl "${SCRIPT_DIR}/filter_reads.pl" "${READS_SAM}" "${FILTERED_SAM}"

# 4. Combine header + filtered reads
cat "${HEADER_SAM}" "${FILTERED_SAM}" > "${COMBINED_SAM}"

# 5. Convert to BAM
samtools view -hbS "${COMBINED_SAM}" -o "${BAM_UNSORTED}"

# 6. Sort by name (required for bamtobed -bedpe)
samtools sort -n -o "${NAMESORT_BAM}" -T "${BAM2BED_DIR}/${OUT_PREFIX}.tmp" "${BAM_UNSORTED}"

# 7. Convert to BEDPE
bedtools bamtobed -i "${NAMESORT_BAM}" -bedpe -mate1 > "${TEMP_BEDPE}"

# 8. Convert BEDPE to BED
perl "${SCRIPT_DIR}/bedpe_to_bed.pl" "${TEMP_BEDPE}" "${BED_FILE}"

echo "Stage 1 complete: ${BED_FILE}"

# === Stage 2: BED deduplication ===
echo "=== Stage 2: BED deduplication ==="

RMDUP_BED="${BAM2BED_DIR}/${OUT_PREFIX}.rmdup.bed"
bash "${SCRIPT_DIR}/deduplicate_bed.sh" "${BED_FILE}" "${RMDUP_BED}"

echo "Stage 2 complete: ${RMDUP_BED}"

# Cleanup intermediate bam2bed files (keep BED_FILE and RMDUP_BED)
rm -f "${HEADER_SAM}" "${READS_SAM}" "${FILTERED_SAM}" "${COMBINED_SAM}" \
      "${BAM_UNSORTED}" "${NAMESORT_BAM}" "${TEMP_BEDPE}"

# Validate BED file is non-empty
if [ ! -s "${RMDUP_BED}" ]; then
    echo "ERROR: Deduplicated BED file is empty. No mapped reads passed filtering."
    exit 1
fi

# === Stages 3-6: Peak analysis (depth 0-10) ===
echo "=== Stages 3-6: Peak analysis (depth 0-10) ==="

for d in $(seq 0 10); do
    echo "--- Depth d=${d} ---"

    PEAK_MERGE="${BED2PEAK_DIR}/${OUT_PREFIX}.d${d}.peak.merge.txt"
    ALL_PEAKS="${BED2PEAK_DIR}/${OUT_PREFIX}.d${d}.all_peaks.txt"
    PEAK_MERGE2="${BED2PEAK_DIR}/${OUT_PREFIX}.d${d}.peak.merge.2.txt"
    PEAK_MERGE3="${BED2PEAK_DIR}/${OUT_PREFIX}.d${d}.peak.merge.3.txt"
    PEAK_XLSX="${BED2PEAK_DIR}/${OUT_PREFIX}.d${d}.peak.merge.xlsx"

    # Stage 3: Peak detection (all peaks)
    bash "${SCRIPT_DIR}/all_peaks.sh" \
        "${RMDUP_BED}" "${OUT_PREFIX}" "${BAM2BED_DIR}" "${ALL_PEAKS}"

    # Stage 4: Peak merging
    bash "${SCRIPT_DIR}/merge_peaks.sh" \
        "${RMDUP_BED}" "${OUT_PREFIX}" "${d}" "${BAM2BED_DIR}" "${PEAK_MERGE}"

    # Stage 4b: Windowed intersection with known sites
    bedtools window -w "${d}" -a "${PEAK_MERGE}" -b "${KNOWN_SITES}" -sm -c > "${PEAK_MERGE2}"

    # Stage 5: Gene annotation
    Rscript "${SCRIPT_DIR}/peak_annotation_step1.R" \
        "${PEAK_MERGE2}" "${PEAK_MERGE3}" "${GENOME}" \
        "${PROMOTER_LEFT}" "${PROMOTER_RIGHT}" "${ENHANCER_LEFT}"

    # Stage 6: Excel export
    Rscript "${SCRIPT_DIR}/peak_annotation_step2.R" \
        "${PEAK_MERGE3}" "${PEAK_XLSX}"

    echo "Depth d=${d} complete: ${PEAK_XLSX}"
done

echo "=== Site analysis pipeline complete ==="
