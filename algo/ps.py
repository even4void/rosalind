#!/usr/bin/env python3

with open("ps.txt") as f:
    next(f)
    lst = [int(x) for x in f.read().split()]

k = lst[-1]
lst = lst[:-1]

print(' '.join(map(str, sorted(lst)[:k])))
