#!/usr/bin/env python3
'''
Title: concatenate_seqs_w_same_id.py
Date: 2020-03-11
Author: Alma Hurtig

Description:
    This program takes a fasta file as input and produce an output file with
    unique ids only (by conatenating all sequences with identical ids). The id
    could for example be a specific species and the sequence lines a gene.

Procedure:
1. Loop through the file and add new ids as keys to the dictionary whenever they occur.
2. Print the sequence that belong to the id to a list and assign it as the value of its id.
3. If an id that already exist in the dictionary occcur, concatenate its sequence
with the list of the previously printed sequence(s) beloning to the same id.
By doing so, sequences with the same id will be concatenated.
4. Print ids and their corresponging sequence to the output file.

Usage: ./concatenate_seqs_w_same_id.py input_fasta output_fasta

'''

import sys

if len(sys.argv) != 3:
    error_msg ='ERROR: Exactly two input arguments are needed.''\n''Usage: ./concatenate_seqs_w_same_id.py input_fasta output_fasta'
    print(error_msg, file = sys.stderr)
    sys.exit()

with open (sys.argv[1], 'r') as fasta_in:
    all = {}
    for line in fasta_in:
        if line.startswith('>'):
            ids = line.split()[0] #assign the id-line to an id
            if ids not in all:
                all[ids]=[] #put new ids as keys and assign an empty list to them
        else:
            seq = line.rstrip()
            all[ids].append(seq) #fill the list with the sequence that follow the id-line, if the id already exist the sequence will be added after the previous sequences

with open(sys.argv[2], 'w') as fasta_out:
    for ids in all:
        fasta_out.write('{}\n{}\n'.format(ids,''.join(all[ids])))
