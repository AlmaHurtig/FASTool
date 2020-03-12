#!/usr/bin/env python3

'''
Title: quick_quality.py
Date: 2020-03-11
Author: Alma Hurtig

Description:
    This program takes a fastq file as input and output the average
    quality of each id. The output quality score range from 1 to 94 where a high
    score equals high quality.

Procedure:
1. Assign quality scores to possible characters in a dictionary
2. Loop through the input fastq file and add id lines and their corresponding quality to an id_quality dictionary.
3. Divide the overall quality of each line by the number of characters in it to obtain the average quality.
4. Print ids with their average quality to a new file (one id per line).

Usage:  ./quick.quality.py fastq_file quality_scores.txt

'''

import sys

if len(sys.argv) != 3:
    error_msg ='ERROR: Exactly three input arguments are needed.''\n''Usage: ./quick.quality.py fastq_file quality_scores.txt'
    print(error_msg, file = sys.stderr)
    sys.exit()

fastq_symbols = {"!": 1,'"': 2, "#": 3, "$": 4, "%": 5, "&": 6, "'": 7, "(": 8,
")": 9, "*": 10, "+": 11, ",": 12, "-": 13, ".": 14, "/": 15, "0": 16, "1": 17,
"2": 18, "3": 19, "4": 20, "5": 21, "6": 22, "7": 23, "8": 24, "9": 25, ":": 26,
";": 27, "<": 28, "=": 29, ">": 30, "?": 31, "@": 32, "A": 33, "B": 34, "C": 35,
"D": 36, "E": 37, "F": 38, "G": 39, "H": 40, "I": 41, "J": 42, "K": 43, "L": 44,
"M": 45, "N": 46, "O": 47, "P": 48, "Q": 49, "R": 50, "S": 51, "T": 52, "U": 53,
"V": 54, "W": 55, "X": 56, "Y": 57, "Z": 58, "[": 59, "\\": 60, "]": 61, "^": 62,
"_": 63, "`": 64, "a": 65, "b": 66, "c": 67, "d": 68, "e": 69, "f": 70, "g": 71,
"h": 72, "i": 73, "j": 74, "k": 75, "l": 76, "m": 77, "n": 78, "o": 79, "p": 80,
"q": 81, "r": 82, "s": 83, "t": 84, "u": 85, "v": 86, "w": 87, "x": 88, "y": 89,
"z": 90, "{": 91, "|": 92, "}": 93, "~": 94}

id_quality = {}

with open(sys.argv[1], "r") as fastq:
    for no, line in enumerate(fastq):
        line = line.rstrip()
        characters = 0
        quality = 0
        if no % 4 == 0: #id line
            id = line.split()[0]
            if id not in id_quality:
                id_quality[id]= 0   #include id in dictionary
        elif no % 4 == 3:   #quality line
            for symbol in line: #loop through the quality line symbol by symbol
                characters += 1    #keep track of the number of characters
                if symbol in fastq_symbols:
                    quality += fastq_symbols[symbol]    #add value of the specific character to the overall quality
            id_quality[id] = (round((quality/characters),2)) #divide the overall quality with the number of characters to get the average quality of the seq

with open(sys.argv[2], 'w') as output:
    for key, value in id_quality.items():
        print(key, ':', value, file=output)
