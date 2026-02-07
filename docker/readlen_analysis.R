#!/usr/bin/env Rscript
args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
  stop("Usage: readlen_analysis.R <fastq1> [fastq2 ...] <output.pdf>")
}
output_pdf <- args[length(args)]
fastq_files <- args[-length(args)]

library(ggplot2)

pdf(output_pdf, width = 8, height = 6)

for (fq in fastq_files) {
  title_str <- basename(fq)
  cat("📎 Processing", title_str, "...\n")
  con <- gzfile(fq, "rt")
  lines <- readLines(con)
  close(con)
  if (length(lines) == 0) {
    cat("⚠️ Empty file:", title_str, "\n")
    next
  }
  seqs <- lines[seq(2, length(lines), 4)]
  lens <- nchar(seqs)
  tab <- as.data.frame(table(lens), stringsAsFactors = FALSE)
  colnames(tab) <- c("Length", "Count")
  tab$Length <- as.integer(tab$Length)
  tab <- tab[order(tab$Length), ]
  tab$RevCumulative <- rev(cumsum(rev(tab$Count)))
  tab$CumulativeFraction <- tab$RevCumulative / sum(tab$Count)

  p1 <- ggplot(tab, aes(x = Length, y = Count)) +
    geom_col(fill = "steelblue") +
    labs(title = paste(title_str, "- Histogram"),
         x = "Read length (bp)", y = "Read count") +
    theme_minimal()

  p2 <- ggplot(tab, aes(x = Length, y = CumulativeFraction)) +
    geom_line(color = "darkgreen", linewidth = 1) +
    labs(title = paste(title_str, "- Fraction ≥ length"),
         x = "Read length (bp)", y = "Fraction ≥ length") +
    theme_minimal()

  print(p1)
  print(p2)
}

dev.off()
