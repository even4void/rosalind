#!/usr/bin/env python3


from collections import Counter


def maj(lst):
    """"
    >>> items = [8, 7, 7, 7, 1, 7, 3, 7]
    >>> print(maj(items))
    7
    """
    c = Counter(lst)
    val, cnt = c.most_common()[0]
    if cnt > len(lst)/2:
        return int(val)
    else:
        return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    items = []
    with open("maj.txt") as f:
        next(f)
        for line in f:
            items.append(line.strip().split())
    f.close()

    val = [maj(elt) for elt in items]
    print(" ".join([str(x) for x in val]))
