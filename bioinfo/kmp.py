#!/usr/bin/env python3

from Bio import SeqIO


def fail(s):
    f = [0 for i in range(len(s))]
    n = len(s)
    k, j = 1, 0
    while k < n:
        if s[k] == s[j]:
            j += 1
            f[k] = j
            k += 1
        else:
            if j != 0:
                j = f[j-1]
            else:
                f[k] = 0
                k += 1
    return f


seq = SeqIO.read("kmp.txt", "fasta")
print(" ".join(map(str, fail(seq))))
