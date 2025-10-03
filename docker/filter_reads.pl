#!/usr/bin/env perl
use strict;
use warnings;

# Read input file from first argument
my $infile  = shift or die "Usage: $0 <input_file>\n";
my $outfile = shift;  # optional output file

open(my $fh, '<', $infile) or die "Cannot open $infile: $!\n";

# If an output file is provided, print there; else STDOUT
my $out_fh;
if ($outfile) {
    open($out_fh, '>', $outfile) or die "Cannot open $outfile: $!\n";
} else {
    $out_fh = *STDOUT;
}

while (<$fh>) {
    my $line = $_;
    my @rec  = split("\t", $line);
    $rec[5] =~ s/[SH].*//;
    if (!($rec[5] =~ /^[0-9]+$/ && $rec[5] > 6)) {
        print $out_fh $line;
    }
}

close($fh);
close($out_fh) if $outfile;
