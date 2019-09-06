#!/usr/bin/env python3


def two_sum(lst):
    lst = list(lst)
    for t in range(len(lst)):
        if -lst[t] in lst[t+1:]:
            for s in range(t+1, len(lst)):
                if lst[t] == -lst[s]:
                    return [t+1, s+1]
    return [-1]


if __name__ == '__main__':
    with open('2sum.txt') as f:
        next(f)
        lst = [map(int, line.rstrip().split()) for line in f]

    for elt in lst:
        print(" ".join(map(str, two_sum(elt))))
