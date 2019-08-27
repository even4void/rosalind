#!/usr/bin/env python3


def ins(lst, verbose=False):
    """
    >>> import random
    >>> random.seed(101)
    >>> items = [random.randint(0, 20) for x in range(10)]
    >>> print(ins(items, verbose=True))
    24 swaps
    [1, 6, 6, 7, 11, 14, 16, 17, 18, 19]
    """
    op = 0
    for i in range(1, len(lst)):
        cur = lst[i]
        k = i - 1
        while k >= 0 and cur < lst[k]:
            lst[k+1] = lst[k]
            op += 1
            k -= 1
        lst[k+1] = cur
    if verbose:
        print("%s swaps" % op)
    return lst


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open('ins.txt') as f:
        for line in f:
            exec(line)

    print(ins(items, verbose=True))
