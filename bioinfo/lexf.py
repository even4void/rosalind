#!/usr/bin/env python3

from functools import cmp_to_key
from itertools import product


def compare(a, b):
    for i in range(len(a) + 1):
        diff = table[a[i]] - table[b[i]]
        if diff == 0:
            continue
        return diff
    return 0


data = open("lexf.txt").read()
val = data.strip().split()
xs, n = (val[:-1], int(val[-1]))

table = dict((e, i) for i, e in enumerate(xs))

res = sorted(product(xs, repeat=n), key=cmp_to_key(compare))

print('\n'.join(map(''.join, res)))
