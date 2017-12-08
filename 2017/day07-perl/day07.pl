#!/usr/bin/env perl
use strict;
use warnings;

my @array;
open(my $fh, "<", "day07.input")
    or die "Failed to open file: $!\n";
while(<$fh>) { 
    chomp; 
    push @array, $_;
} 
close $fh;

my %towers;
my @words;
my @arr;
my @subwords;


my %nodes=();

for my $el (@array) {
    #print $el,"\n";
    
    @words = split /->/, $el;
    @arr = split / /, $words[0];

    #print @words,"\n";

    #create new node record if doesnt exist
    if (!exists $nodes{@arr[0]}) {
        @arr[0] =~ s/^\s+|\s+$//g;
        $nodes{@arr[0]}=0;
    }
    
    # if node has children
    if (@words[1]) {
        #print @words[1];
         @subwords = split /, /,@words[1];

        for my $leaf (@subwords) {
                $leaf =~ s/^\s+|\s+$//g;
                $nodes{$leaf}=33;
        }

    }


}

foreach my $key (keys %nodes) {
        if ($nodes{$key}<1){
          print "answer ",$nodes{$key}," " ,$key, "\n";
        }
    }


#print %nodes,"\n"

