#!/usr/bin/env python3

from Bio import SeqIO
from collections import Counter


def kmer(k, seq):
    K = []
    for i in range(len(seq) - k + 1):
        K.append(seq[i:i+k])
    return K


s = SeqIO.read("kmer.txt", 'fasta')
val = kmer(4, str(s.seq))
val.sort()

cnt = Counter()
for v in val:
    cnt[v] += 1

print(" ".join([str(x) for x in cnt.values()]))
