#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
  stop("Usage: peak_annotation_step2.R <input_file> <output_file>")
}

input_file <- args[1]
output_file <- args[2]

tryCatch({
  # Load required library
  library("xlsx")
  options(stringsAsFactors = FALSE)

  # Read annotated peaks
  inputBed <- read.table(input_file,
                         sep = "\t",
                         header = TRUE,
                         check.names = FALSE)

  # Filter by read support
  inputBed <- subset(inputBed, nUniqueReads > 1 | nReads > 5)

  # Calculate percentages
  inputBed[["percent"]] <- with(inputBed,
                                round(100 * nUniqueReads / sum(nUniqueReads), 2))
  inputBed[["percentAllReads"]] <- with(inputBed,
                                        round(100 * nReads / sum(nReads), 2))

  # Export to Excel
  write.xlsx(inputBed,
             file = output_file)

}, error = function(e) {
  cat("Error in peak_annotation_step2.R:", conditionMessage(e), "\n")
  quit(status = 1)
})
