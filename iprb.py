#!/usr/bin/env python3

# Problem 7
# Given: Three positive integers k, m, and n, representing a population containing
# k+m+n organisms: k individuals are homozygous dominant for a factor, m are
# heterozygous, and n are homozygous recessive.
#  Return: The probability that two randomly selected mating organisms will produce
# an individual possessing a dominant allele (and thus displaying the dominant
# phenotype). Assume that any two organisms can mate.

k, m, n = 29, 15, 28
t = sum([k, m, n])

sample = [k*(k-1),        # AA x AA
          k*m,            # AA x Aa
          k*n,            # AA x aa
          m*k,            # Aa x AA
          m*(m-1)*0.75,   # Aa x Aa
          m*n*0.5,        # Aa x aa
          n*k,            # aa x AA
          n*m*0.5,        # aa x Aa
          n*(n-1)*0]      # aa x aa

print(round(sum(sample)/t/(t-1), 5))
