#!/usr/bin/env python3

from functools import reduce

# see `codons' in `prot.py'
codons = {"A": 4, "C": 2, "D": 2, "E": 2,
          "F": 2, "G": 4, "H": 2, "I": 3,
          "K": 2, "L": 6, "M": 1, "N": 2,
          "P": 4, "Q": 2, "R": 6, "S": 6,
          "T": 4, "V": 4, "W": 1, "Y": 2,
          "Stop": 3}

m = 1000000
seq = "".join(open("mrna.txt").read().split())
f = (codons[x] for x in seq)
print(reduce(lambda a, b: (a * b) % m, f, codons["Stop"]))
