#!/usr/bin/env python3

with open("seto.txt", "r") as fh:
    n = int(fh.readline().strip())
    a = set(map(int, fh.readline().strip()[1:-1].split(", ")))
    b = set(map(int, fh.readline().strip()[1:-1].split(", ")))

r = (set.union(a, b),
     set.intersection(a, b),
     set.difference(a, b),
     set.difference(b, a),
     set.difference(set(range(1, n+1)), a),
     set.difference(set(range(1, n+1)), b))

print("\n".join(map(str, r)))
