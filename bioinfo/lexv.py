#!/usr/bin/env python3

from itertools import product


def gen_str(a, n):
    strings = []
    for i in range(1, n+1):
        strings += [''.join(j) for j in product(a, repeat=i)]

    strings = sorted(strings, key=lambda x: [a.index(k) for k in x])

    return strings


with open("lexv.txt", "r") as f:
    a = f.readline().strip().split(" ")
    n = int(f.readline())

s = gen_str(a, n)
print("\n".join(s))
