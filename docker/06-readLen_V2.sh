Can you update this script so that it orders them correctly?
#!/bin/bash
#
#BSUB -P insertionSite
#BSUB -J readLen
#BSUB -W 40:00
#BSUB -R "rusage[mem=8000]"
#BSUB -e errors.%J.readLen
#BSUB -o output.%J.readLen

echo "🔍 Calculating read length distributions..."

# Generate .readLen files from .fastq.gz files
for fq in newFastq/*.fastq.gz; do
    fq_basename=$(basename "$fq")
    out="newFastq/${fq_basename}.readLen"
    echo "📎 Processing $fq_basename..."
    zcat "$fq" | paste - - - - | cut -f2 | \
        awk '{print length($0)}' | sort | uniq -c | \
	awk '{print $1, $2}' | sort -k2,2n > "$out"
done

# Plotting with R
R --slave <<'EOF'
options(stringsAsFactors = FALSE)
library(ggplot2)

cat("📊 Generating read length plots...\n")
pdf("newFastq/readLen.pdf", width = 8, height = 6)

files <- list.files("newFastq", pattern = "\\.readLen$", full.names = TRUE)

if (length(files) == 0) {
  cat("❌ No .readLen files found.\n")
} else {
  for (f in files) {
    title_str <- basename(f)
    cat("📈 Plotting", title_str, "...\n")
    dat <- tryCatch(read.table(f, header = FALSE), error=function(e) NULL)

    if (!is.null(dat) && nrow(dat) > 0) {
      colnames(dat) <- c("Count", "Length")

      # ✅ Sort by increasing length
      dat <- dat[order(dat$Length), ]

      # ✅ Calculate cumulative fraction of reads ≥ Length
      dat$RevCumulative <- rev(cumsum(rev(dat$Count)))
      dat$CumulativeFraction <- dat$RevCumulative / sum(dat$Count)

      # Plot A: histogram of read lengths
	p1 <- ggplot(dat, aes(x = Length, y = Count)) +
  		geom_col(fill = "steelblue") +
  		labs(title = paste(title_str, "- Histogram"),
       		x = "Read length (bp)", y = "Read count") +
 	 theme_minimal()

	# Plot B: cumulative fraction plot (as before)
	p2 <- ggplot(dat, aes(x = Length, y = CumulativeFraction)) +
	  	geom_line(color = "darkgreen", linewidth = 1) +
	  	labs(title = paste(title_str, "- Fraction ≥ length"),
	       	x = "Read length (bp)", y = "Fraction ≥ length") +
	theme_minimal()

	print(p1)
	print(p2)

    } else {
      cat("⚠️ Skipped empty or invalid file:", title_str, "\n")
    }
  }
}
dev.off()
EOF

