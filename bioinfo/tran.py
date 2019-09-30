#!/usr/bin/env python3

from Bio import SeqIO

s = list(SeqIO.parse("tran.txt", 'fasta'))
s1, s2 = str(s[0].seq), str(s[1].seq)


def foo(s1, s2):
    t1, t2 = 0, 0
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            if s1[i] == 'A' and s2[i] == 'G':
                t1 += 1
            elif s1[i] == 'G' and s2[i] == 'A':
                t1 += 1
            elif s1[i] == 'C' and s2[i] == 'T':
                t1 += 1
            elif s1[i] == 'T' and s2[i] == 'C':
                t1 += 1
            else:
                t2 += 1
    return t1 / t2


print(round(foo(s1, s2), 11))
