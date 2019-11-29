#!/usr/bin/env python3

from Bio import SeqIO


def sub(s, t):
    idx = []
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            idx.append(i + 1)
            j += 1
        i += 1
    return idx


f = open("sseq.txt")
s = []
for elt in SeqIO.parse(f, "fasta"):
    s.append(str(elt.seq))
f.close()

print(" ".join(map(str, sub(s[0], s[1]))))
