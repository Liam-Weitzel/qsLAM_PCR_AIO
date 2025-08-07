#!/bin/bash
#BSUB -P insertionSite
#BSUB -J peakAnnotate
#BSUB -W 10:00
#BSUB -n 1
#BSUB -R "rusage[mem=8000]"
#BSUB -e errors.%J
#BSUB -o output.%J

# Exit on error
set -e

# Create output directories if they don't exist
for d in $(seq 0 10); do
    mkdir -p "bed2peak_${d}"
done

# Process each depth level
for d in $(seq 0 10); do
    # Process each rmdup.bed file
    find bam2bed -name '*rmdup.bed' | while read -r i; do
        out_prefix=$(basename "$i" .bed)
        echo "Processing: $out_prefix at depth $d"

        # Check if input file exists
        if [ ! -f "bed2peak_${d}/${out_prefix}.peak.merge.2.txt" ]; then
            echo "Error: Missing input file bed2peak_${d}/${out_prefix}.peak.merge.2.txt"
            continue
        fi

        # First R script - Gene prediction
        R --slave --no-save --no-restore <<EOF || { echo "R script 1 failed"; continue; }
        tryCatch({
            source("target_gene_prediction.R")
            
            # Read input data
            inputBed <- read.table("bed2peak_${d}/${out_prefix}.peak.merge.2.txt", 
                                 sep="\t", 
                                 check.names=FALSE)
            
            # Add nOverlapWithSpike column with zeros
            inputBed\$V8 <- 0
            
            # Assign column names
            colnames(inputBed) <- c("seqnames", "start", "end", "name", 
                                  "nUniqueReads", "strand", "nReads", 
                                  "nOverlapWithSpike")
            
            inputBed[["name"]] <- gsub("-", ".", 
                                     paste("X", inputBed[["name"]], 
                                     1:nrow(inputBed), sep="_"))
            
            d <- target_gene_prediction(inputBed)
            inputBed <- inputBed[order(inputBed\$name),]
            
            rownames(d) <- d[["peak_id"]]
            inputBed[["gene"]] <- d[inputBed[["name"]], "nearest_gene_symbol"]
            inputBed[["tss_distances"]] <- d[inputBed[["name"]], "tss_distances"]
            inputBed[["gene_region"]] <- d[inputBed[["name"]], "gene_region"]
            inputBed[["name"]] <- sub("^X_", "", inputBed[["name"]])
            inputBed <- inputBed[order(inputBed[["nUniqueReads"]], decreasing=TRUE),]
            
            write.table(inputBed, 
                       file="bed2peak_${d}/${out_prefix}.peak.merge.3.txt",
                       sep="\t",
                       quote=FALSE,
                       row.names=FALSE)
        }, error=function(e) {
            cat("Error in R script 1:", conditionMessage(e), "\n")
            print("Debug information:")
            if(exists("inputBed")) {
                print(str(inputBed))
                print(colnames(inputBed))
            }
            q(status=1)
        })
EOF

        # Second R script remains unchanged
        R --slave --no-save --no-restore <<EOF || { echo "R script 2 failed"; continue; }
        tryCatch({
            library("xlsx")
            options(stringsAsFactors = FALSE)
            
            inputBed <- read.table("bed2peak_${d}/${out_prefix}.peak.merge.3.txt",
                                 sep="\t",
                                 header=TRUE,
                                 check.names=FALSE)
            
            inputBed <- subset(inputBed, nUniqueReads > 1 | nReads > 5)
            
            inputBed[["percent"]] <- with(inputBed, 
                                        round(100 * nUniqueReads/sum(nUniqueReads), 2))
            
            inputBed[["percentAllReads"]] <- with(inputBed,
                                                 round(100 * nReads/sum(nReads), 2))
            
            write.xlsx(inputBed,
                      file="bed2peak_${d}/${out_prefix}.peak.merge.xlsx")
            
        }, error=function(e) {
            cat("Error in R script 2:", conditionMessage(e), "\n")
            q(status=1)
        })
EOF
    done
done
