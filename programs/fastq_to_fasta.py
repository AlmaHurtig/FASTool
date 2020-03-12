#!/usr/bin/env python3

'''
Title: fasta_to_fastq.py
Date: 2020-03-09
Author: Alma Hurtig

Description:
    This program convert a fastq-file to a fasta-file

Procedure:
1. Open the fastq input file and initiate an enumerator
2. Print id-lines (exchange '@' to '>') and sequences to the output file


Usage: ./fastq_to_fasta.py fastq_file output_fasta

'''

import sys

if len(sys.argv) != 3:
    error_msg ='ERROR: Exactly three input arguments are needed.''\n''Usage: ./fastq_to_fasta.py fastq_file output_fasta'
    print(error_msg, file = sys.stderr)
    sys.exit()

with open (sys.argv[1], 'r') as fastq, open (sys.argv[2], 'w') as fasta:
    fastq_read = fastq.readlines()
    for no, line in enumerate(fastq_read):
        line = line.rstrip()
        if no % 4 == 0:
            id_line = line.replace('@', '>', 1) #replace only first occurrance
            fasta.write(id_line)
        elif no % 4 == 1:
            fasta.write(line)
