#!/usr/bin/env python3

'''
Title: translate_all_six_frames.py
Date: 2019-10-30
Author: Alma Hurtig

Description:
    This program translate a given nucleotide sequence to protein sequence and print
    all six possible reading frames.

List of functions:
    'reverse': reverse a given sequence
    'complement': create a complement of the given nucleotide sequence
    'reverse_complement': combine the two functions 'reverse' and 'complement'
    and print the reverse complement of the given DNA sequence

List of "non standard" modules:
    No "non standard" modules were used

Procedure:
1. Create a dictionary with codons as keys and their corresponding amino acid as
value.
2. Create a reverse complement of the given nucleotide sequence and save it to the
variable 'reverse_strand'.
3. Translate the nucleotide sequence and its reversed complement to protein sequences
by looping through the nucleotides and translate one codon at the time.
4. Return all six frames to the console.

Usage:
./translate_all_six_frames.py nucleotide_sequence

'''

import sys

if len(sys.argv) != 2:
    error_msg ='Exactly two input arguments are needed: Usage: ./translate_all_six_frames.py nucleotide_sequence'
    print(error_msg, file = sys.stderr)
    sys.exit()


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

def reverse(sequence):
    return sequence[::-1]

def complement(sequence):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    seq_list = list(sequence)
    seq_list = [complement[base] for base in seq_list]
    return ''.join(seq_list)

def reverse_complement(sequence):
    seq = reverse(sequence)
    seq = complement(seq)
    return(seq)

reverse_strand = reverse_complement(sys.argv[1])
print('Reverse complement:', reverse_strand)

def translate_nucleotides(sequence):
    protein_sequence_1 = ''
    protein_sequence_2 = ''
    protein_sequence_3 = ''
    i = 0
    for i in range(0, len(sequence)-2, 3): # len(seq) + 1 - 3 =-2 (1 for python, 3 for )
        if i < len(sequence):
            protein_sequence_1 += amino_acids[sequence[i:i+3]] # key = sequence[i:i+3] (nt + three following)
        if i > len(sequence):
            break
    for i in range(1, len(sequence)-2, 3):
        if i < len(sequence):
            protein_sequence_2 += amino_acids[sequence[i:i+3]]
        if i > len(sequence):
            break
    for i in range(2, len(sequence)-2, 3):
        if i < len(sequence):
            protein_sequence_3 += amino_acids[sequence[i:i+3]]
        elif i > len(sequence):
            break
    return('Frame 1: {} \nFrame 2: {} \nFrame 3: {}'.format(protein_sequence_1, protein_sequence_2, protein_sequence_3))

nuc_seq = (sys.argv[1])

translated_seq = translate_nucleotides(nuc_seq)
print('Forward: \n{}'.format(translated_seq))

translated_seq_rev = translate_nucleotides(reverse_strand)
print('Reverse: \n{}'.format(translated_seq_rev))
