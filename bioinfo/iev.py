#!/usr/bin/env python3

# Given: Six nonnegative integers, each of which does not exceed 20,000. The
# integers correspond to the number of couples in a population possessing each
# genotype pairing for a given factor. In order, the six given integers
# represent the number of couples having the following genotypes:
# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa
# Return: The expected number of offspring displaying the dominant phenotype
# in the next generation, under the assumption that every couple has exactly
# two offspring.

with open('iev.txt') as f:
    pairing = [int(i) for i in f.readline().strip().split()]
    probs = [1, 1, 1, 3/4, 1/2, 0]
    print(sum(2 * [pairing[i] * probs[i] for i in range(len(probs))]))
