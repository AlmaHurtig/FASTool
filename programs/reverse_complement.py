#!/usr/bin/env python3

'''
Title: reverse_complement.py
Date: 2020-03-11
Author: Alma Hurtig

Description:
    This program takes a fasta file as input and output its reverse complement to
    a new file.

Procedure:
1. Create a dictionary with complement bases
2. Loop through the input fasta file and print it's id and reverse
complement sequence to the output file.

Usage:
./reverse_complement.py fasta_file reverse_complement_file

'''

import sys

if len(sys.argv) != 3:
    error_msg ='ERROR: Exactly three input arguments are needed.''\n''Usage: ./reverse_complement.py fasta_file reverse_complement_file'
    print(error_msg, file = sys.stderr)
    sys.exit()

complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}

with open(sys.argv[1], 'r') as sequence, open(sys.argv[2], 'w') as reverse_comp_file:
    for line in sequence:
        line = line.rstrip().upper()
        if line.startswith('>'):
            print(line, file=reverse_comp_file)
        else:
            seq_list = list(line)
            seq_list = [complement[base] for base in seq_list]
            joined_seq =''.join(seq_list)
            reverse = joined_seq[::-1]
            print(reverse, file=reverse_comp_file)
