#!/usr/bin/env python3

import functools


# Note that we use "built-in" memoization, although for those kind of numbers,
# this should not matter. The lru_cache decorator is well described on SO
# (https://stackoverflow.com/a/49883466). The joblib module should also handle
# this well.
# An alternative recursive solution is also provided on SO:
# https://stackoverflow.com/a/38445336.


@functools.lru_cache(None)
def fib(n):
    """
    >>> fib(6)
    8
    """
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print(fib(23))
