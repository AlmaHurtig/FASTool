#!/usr/bin/env python3

'''
Title: multiline_to_singleline.py
Date: 2020-03-09
Author: Alma Hurtig

Description: This program takes a multiline fasta file and output it in single line format.

Procedure:
1. Open input file and output file
2. Loop through the input fasta file, print the id-line and append all sequence lines to a list. When all sequence lines have been read print the list to the output file (and empty it for the next round).
3. Print the last sequence to the file

Usage: ./multiline_to_singleline.py input_fasta output_fasta

'''

import sys

with open (sys.argv[1], 'r') as multiline, open (sys.argv[2], 'w') as singleline:
    sequence = []
    for line in multiline:
        if line.startswith('>'):
            if sequence:
                singleline.write(''.join(sequence) + '\n')
                sequence = []
            singleline.write(line)
        else:
            sequence.append(line.rstrip())
    if sequence:
        singleline.write(''.join(sequence) + '\n')
