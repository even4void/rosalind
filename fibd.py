#!/usr/bin/env python3

# Problem 11
# Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence
# Relations”, which followed the recurrence relation Fn = Fn−1+Fn−2 and assumed
# that each pair of rabbits reaches maturity in one month and produces a single
# pair of offspring (one male, one female) each subsequent month.
# Our aim is to somehow modify this recurrence relation to achieve a dynamic
# programming solution in the case that all rabbits die out after a fixed number
# of months.See Figure 4 for a depiction of a rabbit tree in which rabbits live
# for three months(meaning that they reproduce only twice before dying).
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
