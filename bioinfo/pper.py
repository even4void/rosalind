#!/usr/bin/env python3

from math import factorial


def pper(n, k):
    return factorial(n) / factorial(n - k)


print(int(pper(83, 10) % 1000000))
