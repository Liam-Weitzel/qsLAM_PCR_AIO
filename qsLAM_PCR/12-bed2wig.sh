#!/bin/bash
#BSUB -P insertionSite
#BSUB -J bed2wig
#BSUB -W 10:00
#BSUB -n 1
#BSUB -R "rusage[mem=8000]"
#BSUB -e errors.%J
#BSUB -o output.%J

mkdir -p bed2wig

for i in bam2bed/*.rmdup.bed; do
    out_prefix=$(basename "$i" .bed)
    
    if [ ! -e "bed2wig/${out_prefix}.pos.bw" ]; then
        genomeCoverageBed -i <(sort -k 1,1 -k 2,2n "$i") -bg -g hg19.chrom.sizes -strand + | \
        sort -k1,1 -k2,2n > "bed2wig/${out_prefix}.pos.bedgraph"
        
        bedGraphToBigWig "bed2wig/${out_prefix}.pos.bedgraph" hg19.chrom.sizes "bed2wig/${out_prefix}.pos.bw"
        
        genomeCoverageBed -i <(sort -k 1,1 -k 2,2n "$i") -bg -g hg19.chrom.sizes -strand - | \
        sort -k1,1 -k2,2n > "bed2wig/${out_prefix}.neg.bedgraph"
        
        bedGraphToBigWig "bed2wig/${out_prefix}.neg.bedgraph" hg19.chrom.sizes "bed2wig/${out_prefix}.neg.bw"
    fi
done
