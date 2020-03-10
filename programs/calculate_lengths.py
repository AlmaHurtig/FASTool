#!/usr/bin/env python3

'''
Title: fasta_to_fastq.py
Date: 2020-03-09
Author: Alma Hurtig

Description: This program calculate, average, maximum and minimum sequence lengths of a fasta input file.

Procedure:
1. Get example max/min from the "bash input line"
2. Loop through the fasta file and keep track of the number and length of sequences.
3. If a sequence is longer/shorter than the given min/max or than previous sequences, assign it to be the new min/max.
4. Calculate average by dividing the overall sequence length with the amount of sequences.

Usage: ./calculate_lengths.py single_line_fasta_file start_max start_min

'''

import sys

id_lines = 0
bases = 0
max = int(sys.argv[2])
min = int(sys.argv[3])

with open(sys.argv[1], 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        if line.startswith('>'):
            id_lines += 1
        else:
            seq = 0
            bases += len(line)
            seq = len(line)
            if (seq > max):
                max = seq
            elif (seq < min):
                min = seq
    average = bases/id_lines

    print('Average sequence length:',round(average,2),'\n','Maximum sequence length:',max,'\n','Minimum sequence length:',min )
