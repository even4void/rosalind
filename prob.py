#!/usr/bin/env python3

# Problem xxx
# Given: A DNA string s of length at most 100 bp and an array A containing at
# most 20 numbers between 0 and 1.
# Return: An array B having the same length as A in which B[k] represents the
# common logarithm of the probability that a random string constructed with
# the GC-content found in A[k] will match s exactly.

from math import log10

with open('prob.txt') as f:
    s = f.readline().rstrip()
    gc = map(float, f.readline().rstrip().split())

    res = []
    for val in gc:
        pgc = val/2
        pat = (1-val)/2

        # use an accumulator to update desired Prob
        # FIXME: May be simplified a bit
        p = 1
        for nucl in s:
            if nucl == 'A' or nucl == 'T':
                p *= pat
            else:
                p *= pgc

        res.append('{0:.3f}'.format(log10(p)))

print(' '.join(res))
