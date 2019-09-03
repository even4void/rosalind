#!/usr/bin/env python3

# NOTE(S):
# - Not cheating (see heapq.merge) ;-)
# - There's probably a faster version but we will need
#   a merge sorting algorithm later, so here we go.


def mergesort(lst):
    """
    >>> x = [1, 3, 2, 4, 5, 9, 1]
    >>> mergesort(x)
    [1, 1, 2, 3, 4, 5, 9]
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

    with open('mer.txt') as f:
        for line in f:
            exec(line)
    val = mergesort(A + B)  # type: ignore
    print(" ".join([str(x) for x in val]))
