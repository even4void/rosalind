#!/usr/bin/env python3

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the
# GC-content of that string. Rosalind allows for a default error of 0.001 in
# all decimal answers unless otherwise stated; please see the note on absolute
# error below.

from Bio import SeqIO

# If we were to be a little bit cheating:
# from Bio.SeqUtils import GC


def gc(x):
    """Compute GC content."""
    val = sum([x.seq.count(k) for k in ["G", "C"]]) / len(x.seq) * 100
    return (x.description, val)


records = list(SeqIO.parse("/Users/chl/gc.fas", 'fasta'))

r = max([gc(x) for x in records], key=lambda item: item[1])
print("%s\n%9.6f" % (r[0], r[1]))
