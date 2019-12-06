#!/usr/bin/env python3

from math import ceil


def fround(num, dec = 0, func = ceil):
    return func(num * (10 ** dec)) / float(10 ** dec)


with open("eval.txt") as fh:
	n, seq, gc = fh.readlines()
	n = int(n.strip())
	seq = seq.strip()
	gc = map(float, gc.split())

cc = [seq.count('C') + seq.count('G'),
      seq.count('A') + seq.count('T')]

ss = n - len(seq) + 1

res = [fround((((0.5 * g) ** cc[0]) * ((0.5 * (1 - g)) ** cc[1])) * ss, 3)
       for g in gc]

print(" ".join(map(str, res)))
