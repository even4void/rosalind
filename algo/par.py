#! /usr/bin/env python3


def two_way_partition(a):
    return [x for x in a[1:] if x <= a[0]] + [a[0]] + [x for x in a[1:] if x > a[0]]


with open("par.txt") as f:
    next(f)
    lst = [int(x) for x in f.read().split()]

res = two_way_partition(lst)
print(" ".join(map(str, res)))
