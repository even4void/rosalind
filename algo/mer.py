#!/usr/bin/env python3

# Not cheating (see heapq.merge) ;-)


def mergesort(lst):
    """
    >>> x = [1, 3, 2, 4, 5, 9, 1]
    >>> mergesort(x)
    [1, 1, 2, 3, 4, 5, 9]
    """
    if len(lst) == 1:
        return lst
    z = []
    mid = len(lst) // 2
    x = mergesort(lst[:mid])
    y = mergesort(lst[mid:])
    i, j = 0, 0
    while i < len(x) and j < len(y):
        if x[i] > y[j]:
            z.append(y[j])
            j += 1
        z.append(x[i])
        i += 1
    z += x[i:]
    z += y[j:]
    return z


if __name__ == '__main__':
    import doctest
    doctest.testmod()

