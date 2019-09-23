#!/usr/bin/env python3

from Bio import SeqIO


def reverse_complement(s):
    """Reverse complement (see `revc.py')."""
    sub = str.maketrans("ATGC", "TACG")
    return s[::-1].translate(sub)


def lookup(s):
    """Lookup table."""
    for i in range(4, 13):
        for j in range(len(s) - i + 1):
            if s[j:j+i] == reverse_complement(s[j:j+i]):
                yield j, s[j:j+i]


s = [str(x.seq) for x in SeqIO.parse("revp.txt", "fasta")]

for k in s:
    for i, j in sorted(lookup(k)):
        print(i+1, len(j))
