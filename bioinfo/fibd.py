#!/usr/bin/env python3

# Given: Positive integers n≤100.
# Return: The total number of pairs of rabbits that will remain after the n-th
# month if all rabbits live for m months.


def wabbits2(n, k=1):
    """Fibonacci with step k and survival time."""
    ages = [1] + [0] * (k - 1)
    for i in range(n - 1):
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)


wabbits2(98, 18)
