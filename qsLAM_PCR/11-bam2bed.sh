#!/bin/bash
#BSUB -P insertionSite
#BSUB -J bam2bed
#BSUB -W 10:00
#BSUB -n 1
#BSUB -R "rusage[mem=8000]"
#BSUB -e errors.%J
#BSUB -o output.%J

# Create output directory if it doesn't exist
mkdir -p bam2bed

for i in bwa/*.bam; do
    # Get basename without .bam extension
    out_prefix=$(basename "$i" .bam)
    echo "Processing: $out_prefix"
    
    if [ ! -e "bam2bed/${out_prefix}.rmdup.bed" ]; then
        # Extract header
        samtools view -H "$i" > "bam2bed/${out_prefix}.sam"
        
        # Filter reads
        samtools view -F 4 "$i" | \
        perl -ne '$line=$_; @rec=split("\t",$line); $rec[5]=~ s/[SH].*//; 
            if(!($rec[5] =~ /^[0-9]+$/ && $rec[5] > 6)){print $line;}' \
            >> "bam2bed/${out_prefix}.sam"
        
        # Convert to BAM and sort by name
        samtools view -hbS "bam2bed/${out_prefix}.sam" | \
        samtools sort -n -o "bam2bed/${out_prefix}.sorted.bam" -T "bam2bed/${out_prefix}.tmp" -
        
        # Convert to BEDPE
        bedtools bamtobed -i "bam2bed/${out_prefix}.sorted.bam" -bedpe -mate1 > "bam2bed/${out_prefix}.temp"
        
        # Process BEDPE to BED
        cat "bam2bed/${out_prefix}.temp" | \
        perl -e 'while(<STDIN>){
            $line=$_; 
            @rec=split("\t", $line); 
            if($rec[0] eq $rec[3]){ 
                $start = ($rec[1], $rec[4])[$rec[1] > $rec[4]]; 
                $end = ($rec[2], $rec[5])[$rec[2] < $rec[5]]; 
                print "$rec[0]\t$start\t$end\t$rec[6]\t$rec[7]\t$rec[8]\n";
            }
        }' | awk -F "\t" '{if(($3-$2)<1000){print}}' > "bam2bed/${out_prefix}.bed"
        
        # Remove duplicates
        cut -f 1,2,3,6 "bam2bed/${out_prefix}.bed" | \
        sort -u | \
        awk '{print $1"\t"$2"\t"$3"\t.\t.\t"$4}' > "bam2bed/${out_prefix}.rmdup.bed"
        
        # Cleanup temporary files
        rm -f "bam2bed/${out_prefix}.temp" "bam2bed/${out_prefix}.sorted.bam"
    fi
done
