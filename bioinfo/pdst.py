#!/usr/bin/env python3

from Bio import SeqIO


def pdist(s1, s2):
    """ Compute the p-distance between s1 and s2. """
    assert len(s1) == len(s2)

    val = sum(1 if s1[i] != s2[i] else 0 for i in range(len(s1))) / len(s1)

    return val


def dpdist(seq):
    """ Compute a matrix of p-distance for a DNA sequence. """
    m = [[0 for i in range(len(seq))] for j in range(len(seq))]

    for i in range(len(seq)):
        for j in range(len(seq)):
            d = f"{float(pdist(seq[i], seq[j])):.5f}"
            m[i][j] = d

    return m


f = open("pdst.txt")
s = []
for elt in SeqIO.parse(f, "fasta"):
    s.append(str(elt.seq))
f.close()

out = dpdist(s)
for line in out:
    print(' '.join(map(str, line)), end="\n")
