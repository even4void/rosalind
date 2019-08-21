#!/usr/bin/env python3

# Given: A collection of DNA strings in FASTA format having total length
# at most 10 kbp.
# Return: The adjacency list corresponding to O3. You may return edges
# in any order.

from Bio import SeqIO
from itertools import product


def overlap(s1, s2, k):
    """Check whether k-suffix of s1 equals k-prefix of s2."""
    return s1[-k:] == s2[:k]


def adjacency(seq, k=3):
    """Compute adjacency list of order k for a dict of sequences."""
    edges = []
    itr = [(a, b) for [a, b] in product(records, repeat=2) if a is not b]
    for u, v in itr:
        us, vs = str(seq[u].seq), str(seq[v].seq)

        if overlap(us, vs, k):
            edges.append((u, v))

    return edges


records = SeqIO.to_dict(SeqIO.parse("grph.txt", "fasta"))
print('\n'.join([' '.join([a, b]) for (a, b) in adjacency(records, 3)]))
