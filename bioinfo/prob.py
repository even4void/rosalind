#!/usr/bin/env python3

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
        p = 1
        for nucl in s:
            p *= pat if nucl in ['A', 'T'] else pgc
        res.append('{0:.3f}'.format(log10(p)))

print(' '.join(res))
