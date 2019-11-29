#!/usr/bin/env python3

from functools import reduce


def prob(N, gc, rna):
    mapping = {"G": gc/2.0, "C": gc/2.0,
               "A": (1.0-gc)/2.0, "T": (1.0-gc)/2.0}
    value = reduce(lambda x, y: x * mapping[y], list(rna), 1.0)
    p = 1.0 - value
    return round(1.0 - p**N, 3)


N = 95782
gc = 0.462799
rna = "TGTGGGTA"

print(prob(N, gc, rna))
