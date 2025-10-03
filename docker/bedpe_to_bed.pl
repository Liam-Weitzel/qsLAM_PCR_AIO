#!/usr/bin/env perl
use strict;
use warnings;

# Usage: bedpe_to_bed.pl <input_file> <output_file>
my $infile  = shift or die "Usage: $0 <input_file> <output_file>\n";
my $outfile = shift or die "Usage: $0 <input_file> <output_file>\n";

open(my $fh_in,  '<', $infile)  or die "Cannot open $infile: $!\n";
open(my $fh_out, '>', $outfile) or die "Cannot open $outfile: $!\n";

while (<$fh_in>) {
    my $line = $_;
    my @rec  = split("\t", $line);
    if ($rec[0] eq $rec[3]) {
        my $start = ($rec[1] > $rec[4]) ? $rec[1] : $rec[4];
        my $end   = ($rec[2] < $rec[5]) ? $rec[2] : $rec[5];
        print $fh_out "$rec[0]\t$start\t$end\t$rec[6]\t$rec[7]\t$rec[8]\n";
    }
}

close($fh_in);
close($fh_out);
