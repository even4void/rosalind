#!/usr/bin/env python3

# See also hea.py for max-heap.

from heapq import heappush, heappop


def heapsort(xs):
    h = []
    for x in xs:
        heappush(h, x)
    return [heappop(h) for i in range(len(h))]


if __name__ == '__main__':
    with open('hs.txt') as f:
        next(f)
        lst = [int(x) for x in f.read().split()]

    srt = heapsort(lst)
    print(" ".join(map(str, srt)))
