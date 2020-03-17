#!/usr/bin/env python3


'''
Title: translate_sequence.py
Date: 2020-03-16
Author: Alma Hurtig

Description:
    This program translate a given nucleotide sequence to its corresponding
    protein sequence and print it to the stated output file. The input could
    be a single line FASTA file with one sequence only or a textfile including
    a single line nucleotide sequence.

List of functions:
    'translate_nucleotides': translate the nucleotide sequence to its
    corresponding amino acid sequence.

Procedure:
1. Read the file, print its ID (if FASTA file) to the output, extract the sequence
and assign it to a string variable.
2. Translate the nucleotide sequence to its corresponding protein sequences by
looping through the nucleotides and translate one codon at the time.
5. Print the translated sequence to the output file.

Usage:
./translate_sequence.py singleline_fasta output_file

'''
import sys

if len(sys.argv) != 3:
    error_msg ='Exactly three input arguments are needed: Usage: ./translate_sequence.py input_file output_file'
    print(error_msg, file = sys.stderr)
    sys.exit()

output_file = open(sys.argv[2], 'w')

with open(sys.argv[1], 'r') as input:
    nuc_seq = ''
    for line in input:
        line = line.rstrip()
        if line.startswith('>'):
            print(line, file=output_file)   #print the ID to the output file
        else:
            nuc_seq = ''.join(line) #save the sequence in a string variable


def translate_nucleotides(sequence):    #translate the sequence codon by codon
    amino_acids = {"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V",
                "TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V",
                "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V",
                "TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V",
                "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
                "TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
                "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
                "TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
                "TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D",
                "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
                "TAA" : "-", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
                "TAG" : "-", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
                "TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G",
                "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
                "TGA" : "-", "CGA" : "R", "AGA" : "R", "GGA" : "G",
                "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"}
    protein_sequence = ''
    i = 0
    for i in range(0, len(sequence)-2, 3): # len(seq) + 1 - 3 =-2 (1 for python, 3 for codon)
        if i < len(sequence):
            protein_sequence+= amino_acids[sequence[i:i+3]] # key = sequence[i:i+3] (nt + three following)
        if i > len(sequence):
            break
    return('{}'.format(protein_sequence))


translated_seq = translate_nucleotides(nuc_seq)#print translated sequence
print('{}'.format(translated_seq), file=output_file)
