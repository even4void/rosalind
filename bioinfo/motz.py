#!/usr/bin/env python3

from Bio import SeqIO


def motz(seq):
    if len(seq) <= 1:
        return 1
    if seq in matches:
        return matches[seq]
    else:
        matches[seq] = motz(seq[1:])
        for i in range(1, len(seq)):
            if seq[i] == codons[seq[0]]:
                matches[seq] += motz(seq[1:i]) * motz(seq[i+1:])
        return matches[seq]


rna = SeqIO.read("motz.txt", "fasta")
codons = {"A": "U", "U": "A", "C": "G", "G": "C"}
matches = {}

print(motz(str(rna.seq)) % 1000000)
