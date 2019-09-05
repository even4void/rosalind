#!/usr/bin/env python3

from collections import defaultdict


def two_sum(lst, x):
    '''Returns [i,j] such that a[i] + a[j] = x if, otherwise -1.'''
    items = defaultdict(set)

    for i, e in enumerate(lst):
        items[e].add(i)

    for e in items:
        if x - e in items:
            if x - e == e and len(items[e]) > 1:
                return sorted([items[e].pop()+1, items[e].pop()+1])
            else:
                return sorted([items[e].pop()+1, items[x-e].pop()+1])

    return -1


if __name__ == '__main__':
    with open('2sum.txt') as f:
        k, n = map(int, f.readline().rstrip().split())
        lst = [map(int, line.rstrip().split()) for line in f]

    values = [two_sum(x, 0) for x in lst]
    values = [str(x) if type(x) is int
              else ' '.join(map(str, x)) for x in values]
    print('\n'.join(values))
