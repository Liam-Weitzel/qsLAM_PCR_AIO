#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
  stop("Usage: peak_annotation_step1.R <input_file> <output_file>")
}

input_file <- args[1]
output_file <- args[2]

tryCatch({
  # Load target gene prediction function
  source("target_gene_prediction.R")

  # Read input data
  inputBed <- read.table(input_file,
                         sep = "\t",
                         check.names = FALSE)

  # Add nOverlapWithSpike column with zeros
  inputBed$V8 <- 0

  # Assign column names
  colnames(inputBed) <- c("seqnames", "start", "end", "name",
                          "nUniqueReads", "strand", "nReads",
                          "nOverlapWithSpike")

  # Normalize names
  inputBed[["name"]] <- gsub("-", ".",
                             paste("X", inputBed[["name"]],
                                   1:nrow(inputBed), sep = "_"))

  # Run gene prediction
  d <- target_gene_prediction(inputBed)

  # Reorder for mapping
  inputBed <- inputBed[order(inputBed$name), ]
  rownames(d) <- d[["peak_id"]]

  # Map gene annotations back
  inputBed[["gene"]] <- d[inputBed[["name"]], "nearest_gene_symbol"]
  inputBed[["tss_distances"]] <- d[inputBed[["name"]], "tss_distances"]
  inputBed[["gene_region"]] <- d[inputBed[["name"]], "gene_region"]

  # Clean names and sort by read count
  inputBed[["name"]] <- sub("^X_", "", inputBed[["name"]])
  inputBed <- inputBed[order(inputBed[["nUniqueReads"]], decreasing = TRUE), ]

  # Write result
  write.table(inputBed,
              file = output_file,
              sep = "\t",
              quote = FALSE,
              row.names = FALSE)

}, error = function(e) {
  cat("Error in peak_annotation_step1.R:", conditionMessage(e), "\n")
  if (exists("inputBed")) {
    print(str(inputBed))
    print(colnames(inputBed))
  }
  quit(status = 1)
})
