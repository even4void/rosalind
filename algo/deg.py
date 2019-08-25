#!/usr/bin/env python3


from collections import Counter
from itertools import chain


def edges(filename='deg.txt'):
    """
    >>> import sys
    >>> o = sys.stdout
    >>> sys.stdout = open('tmp.txt', 'w')
    >>> print('6 7\\n1 2\\n2 3\\n6 3\\n5 6\\n2 5\\n2 4\\n4 1')
    >>> sys.stdout = o
    >>> d = edges('tmp.txt')
    >>> print(" ".join(str(elt) for elt in [d[k] for k in sorted(d, key=int)]))
    2 4 2 2 2 2
    """
    e = []
    with open(filename) as f:
        next(f)
        for line in f:
            e.append(line.strip().split())
    f.close()

    lst = []
    for x in chain.from_iterable(e):
        lst.append(x)

    return Counter(lst)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    d = edges()
    for k in sorted(d, key=int):
        print(d[k], end=" ")
