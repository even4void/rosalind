#!/usr/bin/env python3

# NOTE See also mer.py, from which the routine below is taken.


def mergesort(lst):
    """
    >>> x = [20, 19, 35, -18, 17, -20, 20, 1, 4, 4]
    >>> mergesort(x)
    [-20, -18, 1, 4, 4, 17, 19, 20, 20, 35]
    """
    if len(lst) <= 1:
        return lst
    z = []
    mid = len(lst) // 2
    x = mergesort(lst[:mid])  # left
    y = mergesort(lst[mid:])  # right
    i, j = 0, 0
    while i < len(x) and j < len(y):
        if x[i] >= y[j]:
            z.append(y[j])
            j += 1
        else:
            z.append(x[i])
            i += 1
    z += x[i:]
    z += y[j:]
    return z


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open('ms.txt') as f:
        next(f)
        for line in f:
            values = map(int, line.split(' '))

    values = mergesort(list(values))
    print(" ".join([str(x) for x in values]))
