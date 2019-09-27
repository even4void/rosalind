#!/usr/bin/env python3

from Bio import SeqIO


def translate(dna, introns):
    introns = sorted(introns, key=len, reverse=True)
    for intron in introns:
        while intron in dna:
            dna = dna.replace(intron, '')
    rna = dna.replace('T', 'U')
    return ''.join([codons[rna[t:t+3]] for t in range(0, len(rna)-2, 3)][:-1])


codons = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
          "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
          "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
          "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
          "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
          "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
          "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
          "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
          "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
          "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
          "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
          "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
          "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
          "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
          "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
          "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}

filename = open("splc.txt", "r")
lines = list(SeqIO.parse(filename, "fasta"))
dna, introns = lines[0], lines[1:]
print(translate(str(dna.seq), [str(x.seq) for x in introns]))
