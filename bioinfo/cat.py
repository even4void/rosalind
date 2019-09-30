#!/usr/bin/env python3

from Bio import SeqIO


c = {"": 1, "A": 0, "C": 0, "G": 0, "U": 0,
     "AA": 0, "AC": 0, "AG": 0, "AU": 1,
     "CA": 0, "CC": 0, "CG": 1, "CU": 0,
     "GA": 0, "GC": 1, "GG": 0, "GU": 0,
     "UA": 1, "UC": 0, "UG": 0, "UU": 0}


seq = SeqIO.read("cat.txt", 'fasta')


def catalan(s):
    if (s not in c):
        if s.count("C") != s.count("G") or s.count("A") != s.count("U"):
            c[s] = 0
        else:
            c[s] = sum([catalan(s[1:i]) * c[s[0]+s[i]] * catalan(s[i+1:])
                        for i in range(1, len(s), 2)])
    return c[s]


print(catalan(seq.seq) % 1000000)
