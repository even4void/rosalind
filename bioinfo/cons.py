#!/usr/bin/env python3

# Problem 10
# A consensus string c is a string of length n formed from our collection
# by taking the most common symbol at each position; the j th symbol of c
# therefore corresponds to the symbol having the maximum value in the j-th
# column of the profile matrix. Of course, there may be more than one most
# common symbol, leading to multiple possible consensus strings.
# Given: A collection of at most 10 DNA strings of equal length (at most 1
# kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If
# several possible consensus strings exist, then you may return any one of
# them.)

# FIXME: Paste the Numpy version I used beforehand.
# My previous attempt was ok but I prefer this very elegant code.
# Credits: BioGeek, https://stackoverflow.com/a/30367656

from Bio import SeqIO
from collections import Counter


def main(fasta_file):
    """Compute a consensus string based on Fasta samples."""
    with open(fasta_file) as fh:
        dna_strings = [str(fasta.seq) for fasta in SeqIO.parse(fh, 'fasta')]
        transposed = zip(*dna_strings)
        counters = [Counter(column) for column in transposed]

        # create consensus
        consensus = ''.join([counter.most_common(1)[0][0] for counter in counters])

        # create profile matrix
        matrix = ''
        for base in 'ACGT':
            matrix += '{}:'.format(base)
            for counter in counters:
                matrix += ' {}'.format(counter[base])
            matrix += '\n'
        matrix = matrix.rstrip()

        return '\n'.join([consensus, matrix])


print(main(r'./cons.txt'))
