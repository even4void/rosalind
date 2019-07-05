#!/usr/bin/env python3

# Problem 1
# A string is simply an ordered collection of symbols selected from
# some alphabet and formed into a word; the length of a string is
# the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the
# symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective
# number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.


from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

raw = "AGAAGTCCTATAGATTGGATCCAATTAGCGTAGAAGTCTGTAAGCGAT \
       ACGACCCCCTTTAGTCGAGTGTCGCCTGAGGGCTTATGTTCTTCGGCG \
       CCCGTAGTGGTGCCAGTTGATTGTCAGCTCCTGACATGGCTACTTCTA \
       ATTGTCTTTTATTACGGGGGGGCCGAGCCTCAGTGTGCCCCCCCCTGT \
       ATTAGCGACAGATTTACCTCTTCGTTAGAAGGAACAACCGAGAGAAGG \
       CCAGGGTGATTAATGCAAGCGGAGCTGACTTGCATCTTTCCTATTAAT \
       AGTATTGACTCCCGTTCCAAAGCGCCGATTATCGGGCACATGTTGATT \
       CATAGGCAACTATGAAATTGAAAGTTATAATGACTGGAAAGGCGGGCA \
       AGACGGCACTCAAGGCACGGACAACGAGCCCGCGAAATCAACTATTGT \
       AGCCGCGATAAACTTAAATTGGAGTAGCGTGGCGTCCGGAATCCAAGA \
       CGGCATACGGGGGTAACAAATGCTAGAAAGATGGAACGCCCCTGAAGT \
       CCCAAGCAAAGGGCCAAATTAACGGTTCCTGCACTACTGCCCGGGGCA \
       GGTCACCTCCTTCTCCATACTCCAATACATGCTGCAGGTAGGCCGATA \
       CTTTACGTGCCCAACGATGACGTTGATTAACCAGCCGTCTCGCAGGGA \
       TACGGCATCGTGAGAGGTGGCCTAGCTGCACAGGCCCCAGTTCATGCT \
       TAAGGTACTCGGTATACAGGAGTGCTAGGCTTATTACTAGCAACCGCC \
       AGTTAACTAACAATATAGTAGCCCCAAGACGGTATTCGCGCCCCTGGT \
       TGCCTTGAGTGTGTATCCGTTCTGCCATGGCACGCTCATAGGGCGATA \
       TCGATACATAACTCACGCACTTAAGGCCACGGGCACGACATGACATAA \
       CACTCTAACCTCTCTTCAATGGCCTATTTCGGCAGCTGGGAAGATGGT \
       GAGATCGGTTTTCGGTGAATATGCCATCA"

s = Seq(raw.replace(" ", ""), generic_dna)

[s.count(x) for x in ["A","C","G","T"]]
