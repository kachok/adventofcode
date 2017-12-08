#!/usr/bin/env perl
use strict;
use warnings;

use Data::Dumper qw(Dumper);

my @towers;

my @array;
open(my $fh, "<", "day07.input")
    or die "Failed to open file: $!\n";
while(<$fh>) { 
    chomp; 
    push @array, $_;
} 
close $fh;

my $i=0;

for my $el (@array) {
    #print $el,"\n";

    my @words = split /->/, $el;
    my @arr = split / /, $words[0];

    #parse weight
    @arr[1] = substr(@arr[1], 1, length(@arr[1])-2);
    #print "arr0 [",@arr[0],"]\n";
    
    #@arr[0] = ~ s/^\s+|\s+$//g;

    my $weight=@arr[1];
    my $tower=@arr[0];

    my @subtowers=();

    # if node has children
    if (@words[1]) {
        #print @words[1];
         my @subwords = split /, /,@words[1];

        for my $sub (@subwords){
            $sub=~ s/^\s+|\s+$//g;
            #print "sub [",$sub,"]\n";
            push(@subtowers,$sub);
        }
        my @data;
        @data=($tower,$weight,0,join(":",@subtowers));
        @towers[$i]=\@data;
    }
    else {

        my @data;
        @data=($tower,$weight,0,"");
        @towers[$i]=\@data;

    }

    $i=$i+1;

}


for my $el (@towers) {
    my @arr=$el;
    print $arr[0][0]," ",$arr[0][1]," ",$arr[0][2]," ",$arr[0][3]," ","\n";
}


my $c=calc("cqmvs");

print "answer: ", $c, "\n";

#calc("mkslglr");

 sub calc {
    my ($tower) = @_;


    print "calculating ",$tower, "\n";
    #print "array ",@towers[0], "\n";
    #print "array searhc ",$towers[0][3], "\n";
    for $i (0 .. $#towers) {        
        my @arr=@towers;
        if ($tower eq $arr[$i][0]) { 
            print ">>> ", $arr[$i][0]," ",$arr[$i][1]," ",$arr[$i][2]," ",$arr[$i][3]," ","\n";
            
            #if it is a leaf return it weight
            if ($arr[$i][3] eq "") {
                return($arr[$i][1]); 
            }
            #if it is a branch, calculate weight of all subbranches
            else {
                my @subtowers = split /:/,$arr[$i][3];
                my $sum=$arr[$i][1];
                my $val=-1;

                my @local;

                my $toexit=0;
                print "starting subs","\n";

                for my $el (@subtowers){
                    my $c=calc($el);
                    push(@local, $c." ".$el);                    
                    if ($val==-1){
                        $val=$c;
                        print "+++",$c,"\n";
                    }
                    else {
                        if ($val!=$c) {
                            print "+++",$c,"\n";
                            $toexit=1;
                        }
                    }
                    $sum=$sum+$c;
                }
                if ($toexit==1) {
                    print "wgh: ",$arr[$i][1]," \n";
                    print "val: ",$val," \n";
                    print "sum: ",$sum," \n";
                    print "local:",@local,"\n";
                    print ">>>EXIT";
                    exit;
                }
                return($sum);
            }
        }
    }

   return(0);
 }

#answer is last line >>> local:2615 vmttcwe2607 ukwlfcf2607 zzpevgd
# look up weight of vmttcwe 2318 - (2615-2607) = 2310