#!/usr/bin/env python3

from Bio import SeqIO
from math import factorial


def nmatch(seq):
    return factorial(seq.count("A")) * factorial(seq.count("C"))


record = SeqIO.read("pmch.txt", "fasta")
print(nmatch(record.seq))
