#!/usr/bin/env python3


def bins(lst, start, end, elt):
    """
    >>> array = [10, 20, 30, 40, 50]
    >>> idx = [40, 10, 35, 15, 40, 20]
    >>> print([bins(array, 0, len(array)-1, x) for x in idx])
    [4, 1, -1, -1, 4, 2]
    """
    mid = (start + end) // 2
    if start > end:
        return -1
    if elt == lst[mid]:
        # simulate 1-based indexing for Rasalind
        return mid+1
    elif elt < lst[mid]:
        return bins(lst, start, mid-1, elt)
    else:
        # elt > lst[mid]
        return bins(lst, mid+1, end, elt)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open('bins.txt') as f:
        for line in f:
            exec(line)

    print([bins(array, 0, len(array)-1, x) for x in idx])
