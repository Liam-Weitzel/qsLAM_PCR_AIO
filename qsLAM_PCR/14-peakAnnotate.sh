#!/bin/bash
#
#BSUB -P insertionSite         # project code
#BSUB -J peakAnnotate      # job name
#BSUB -W 10:00                # wall-clock time (hrs:mins)
#BSUB -n 1      # number of cpu
#BSUB -R "rusage[mem=8000]"     # memory to reserve, in MB
#BSUB -e errors.%J     # error file name in which %J is replaced by the job ID
#BSUB -o output.%J     # output file name in which %J is replaced by the job ID

# module load bedtools/2.25.0
# module load R/3.5.1

# Iterate through different peak calling thresholds
for distance in $(seq 0 10); do
    # Process each BAM to BED file that has been deduplicated
    for bed_file in $(ls -1 bam2bed | grep rmdup.bed); do
        # Remove .bed extension from filename for output naming
        out_prefix=$(echo $bed_file | sed 's/\.bed//')
        echo "Processing: $out_prefix"

        #-----------------------------------------------------------------------
        # First R Script: Target Gene Prediction
        #-----------------------------------------------------------------------
        R --slave <<EOF
        # Source the target gene prediction functions
        source("target_gene_prediction.R")

        # Read the data
        inputBed <- read.table("bed2peak_${distance}/${out_prefix}.peak.merge.2.txt", 
                             sep="\t", 
                             check.names=FALSE)
        
        # Define expected column names
        expected_cols <- c("seqnames", "start", "end", "name", "nUniqueReads", 
                         "strand", "nReads", "nOverlapWithSpike")
        
        # Check if number of columns matches
        if(ncol(inputBed) != length(expected_cols)) {
            print(paste("Error: Expected", length(expected_cols), "columns but found", ncol(inputBed), "columns"))
            print("File:", "${out_prefix}.peak.merge.2.txt")
            quit(status = 1)
        }

        # Assign column names and continue processing
        colnames(inputBed) <- expected_cols
        inputBed[["name"]] <- gsub("-", ".", paste("X", inputBed[["name"]], 1:nrow(inputBed), sep="_"))
        d <- target_gene_prediction(inputBed)
        rownames(d) <- d[["peak_id"]]

        inputBed <- inputBed[order(inputBed\$name),]
        inputBed[["gene"]] <- d[inputBed[["name"]], "nearest_gene_symbol"]
        inputBed[["tss_distances"]] <- d[inputBed[["name"]], "tss_distances"]
        inputBed[["gene_region"]] <- d[inputBed[["name"]], "gene_region"]
        
        inputBed[["name"]] <- sub("^X_", "", inputBed[["name"]])
        inputBed <- inputBed[order(inputBed[["nUniqueReads"]], decreasing=TRUE),]
        
        write.table(inputBed, 
                   file="bed2peak_${distance}/${out_prefix}.peak.merge.3.txt", 
                   sep="\t", 
                   quote=FALSE, 
                   row.names=FALSE)
EOF

        # Check if R script exited with error
        if [ $? -ne 0 ]; then
            echo "Error: Column mismatch detected. Exiting..."
            exit 1
        fi

        #-----------------------------------------------------------------------
        # Second R Script: Excel File Generation
        #-----------------------------------------------------------------------
        R --slave <<EOF
        library("xlsx")
        options(stringsAsFactors = FALSE)

        # Read processed peak data
        inputBed <- read.table("bed2peak_${distance}/${out_prefix}.peak.merge.3.txt", 
                             sep="\t", 
                             header=TRUE, 
                             check.names=FALSE)

        # Filter low-quality peaks
        inputBed <- subset(inputBed, nUniqueReads > 1 | nReads > 5)

        # Calculate percentages for unique reads and all reads
        inputBed[["percent"]] <- round(100 * inputBed[,"nUniqueReads"] / sum(inputBed[,"nUniqueReads"]), 2)
        inputBed[["percentAllReads"]] <- round(100 * inputBed[,"nReads"] / sum(inputBed[,"nReads"]), 2)

        # Save to Excel file
        write.xlsx(inputBed, file="bed2peak_${distance}/${out_prefix}.peak.merge.xlsx")
EOF
    done
done
