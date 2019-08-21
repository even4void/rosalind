#!/usr/bin/env python3

# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each
# in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions
# exist, you may return any single solution.)

from Bio import SeqIO


def long_substr(data):
    """https://stackoverflow.com/a/32611507"""
    substrs = lambda x: {x[i:i+j] for i in range(len(x))
                         for j in range(len(x) - i + 1)}
    s = substrs(data[0])
    for val in data[1:]:
        s.intersection_update(substrs(val))
    return max(s, key=len)


s = [str(x.seq) for x in SeqIO.parse("lcsm.txt", "fasta")]
print(long_substr(s))
