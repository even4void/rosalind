#!/usr/bin/env python3


def sum_deg(filename='ddeg.txt'):
    """
    >>> import sys
    >>> o = sys.stdout
    >>> sys.stdout = open('tmp.txt', 'w')
    >>> print('5 4\\n1 2\\n2 3\\n4 3\\n2 4')
    >>> sys.stdout = o
    >>> d = sum_deg('tmp.txt')
    >>> print(" ".join(str(elt) for elt in [d[k] for k in sorted(d, key=int)]))
    3 5 5 5 0
    """
    with open(filename) as f:
        nv, ne = map(int, f.readline().rstrip().split())
        e = [map(int, line.rstrip().split()) for line in f]

        adj = {k: [] for k in range(1, nv+1)}
        for v1, v2 in e:
            adj[v1].append(v2)
            adj[v2].append(v1)

        ddeg = {k: 0 for k in adj.keys()}
        for v in adj:
            for n in adj[v]:
                ddeg[v] += len(adj[n])

        return ddeg


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    d = sum_deg()
    for k in sorted(d, key=int):
        print(d[k], end=" ")
