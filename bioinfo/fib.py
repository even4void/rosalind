#!/usr/bin/env python3

# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months,
# if we begin with 1 pair and in each generation, every pair of reproduction-
# age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).


def wabbits(n, k):
    """Fibonacci with step of k."""
    a, b = 1, 1
    for i in range(3, n+1):
        a, b = b, a*k + b
    return b


wabbits(35, 3)
