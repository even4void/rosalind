#!/usr/bin/env python3

# NOTE This is basically merge sort while keeping the number of inversions
# in memory at each step.


def mergesort(lst):
    """
    >>> x = [-6, 1, 15, 8, 10]
    >>> xs, inv = mergesort(x)
    >>> inv
    2
    """
    if len(lst) <= 1:
        return lst, 0
    z = []
    mid = len(lst) // 2
    x, xi = mergesort(lst[:mid])  # left
    y, yi = mergesort(lst[mid:])  # right
    i, j = 0, 0
    inv = 0 + xi + yi
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
            inv += len(x)-i
    z += x[i:]
    z += y[j:]
    return z, inv


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open('inv.txt') as f:
        next(f)
        for line in f:
            values = map(int, line.split(' '))

    values, inv = mergesort(list(values))
    print(inv)
