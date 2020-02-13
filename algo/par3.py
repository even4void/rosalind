#! /usr/bin/env python3


def three_way_partition(lst):
    pre, suf, mid = [], [], []
    for elt in lst:
        if elt < lst[0]:
            pre.append(elt)
        elif elt == lst[0]:
            mid.append(elt)
        else:
            suf.append(elt)
    return pre + mid + suf


with open("par3.txt") as f:
    next(f)
    lst = [int(x) for x in f.read().split()]

res = three_way_partition(lst)
print(" ".join(map(str, res)))


