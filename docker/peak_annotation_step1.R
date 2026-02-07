#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 6) {
  stop("Usage: peak_annotation_step1.R <input_file> <output_file> <genome> <promoter.left> <promoter.right> <enhancer.left>")
}

input_file <- args[1]
output_file <- args[2]
genome <- args[3]
promoter.left <- as.numeric(args[4])
promoter.right <- as.numeric(args[5])
enhancer.left <- as.numeric(args[6])

tryCatch({
  # Resolve script directory from Rscript --file= argument
  .script_dir <- dirname(sub("--file=", "", grep("--file=", commandArgs(trailingOnly = FALSE), value = TRUE)))
  source(file.path(.script_dir, "target_gene_prediction.R"))

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
  d <- target_gene_prediction(inputBed, genome, promoter.left, promoter.right, enhancer.left)

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
