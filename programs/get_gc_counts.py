#!/usr/bin/env python3

'''
Title: get_gc_counts.py
Date: 2020-03-10
Author: Alma Hurtig

Description:
    This program takes a fasta-file as input and calculate it's overall and
    codon base position GC-contents (GC, GC1, GC2, GC3).

List of functions:
    'gc_counts': calculate GC, GC1, GC2 and GC3.

Procedure:
1. Loop throught each sequence of the fasta-file base by base and calculate the
number of 'G/C'-bases and 'A/T'-bases
2. Loop through the sequences and read every third base (starting at position
1, 2 and 3 - three different for loops). If the base is a 'G' or 'C' add +1 to
the 'gc' key of the dictionary, if it is 'A' or 'T' add +1 to the 'at' key of
the dictionary.
3. Calculate the four types of GC-contents.
4. Print the output to the console.

Usage: ./get_gc_counts.py fasta_file

'''

import sys

if len(sys.argv) != 2:
    error_msg ='ERROR: Exactly two input arguments are needed.''\n''Usage: ./get_gc_counts.py fasta_file'
    print(error_msg, file = sys.stderr)
    sys.exit()

def gc_counts(fasta):
    gc_c = 0    #used to keep track of overall gc_content
    at_c = 0
    GC1 = {'gc': 0, 'at':0} #one dictionary for each codon position
    GC2 = {'gc': 0, 'at':0}
    GC3 = {'gc': 0, 'at':0}
    for line in fasta:
        line = line.rstrip().upper()
        if not line.startswith('>'):
            my_seq = ''.join(line)
            for letter in my_seq:
                if letter in 'GC':
                    gc_c += 1
                elif letter in 'AT':
                    at_c += 1
            for letter in my_seq[::3]:
                if letter in 'GC':
                    GC1['gc'] += 1
                elif letter in 'AT':
                    GC1['at'] += 1
            for letter in my_seq[1::3]:
                if letter in 'GC':
                    GC2['gc'] += 1
                elif letter in 'AT':
                    GC2['at'] += 1
            for letter in my_seq[2::3]:
                if letter in 'GC':
                    GC3['gc'] += 1
                elif letter in 'AT':
                    GC3['at'] += 1
    GC = round(100 * gc_c / (gc_c + at_c))
    GC1_tot = round(100 * GC1['gc'] / (GC1['gc'] + GC1['at']))
    GC2_tot = round(100 * GC2['gc'] / (GC2['gc'] + GC2['at']))
    GC3_tot = round(100 * GC3['gc'] / (GC3['gc'] + GC3['at']))
    return (GC, GC1_tot, GC2_tot, GC3_tot)

#open input file
fasta_file = open(sys.argv[1], 'r')

#print output to konsole
gc, gc1, gc2, gc3 = gc_counts(fasta_file)
print('GC:','\t',(gc),'%')
print('GC1:','\t',(gc1),'%')
print('GC2:','\t',(gc2),'%')
print('GC3:','\t',(gc3),'%')
