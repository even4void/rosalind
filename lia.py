#!/usr/bin/env python3

# Problem 15
# Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin
# with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children
# in the 1st generation, each of whom has two children, and so on. Each i
# organism always mates with an organism having genotype Aa Bb.
# Return: The probability that at least N Aa Bb organisms will belong to the
# k-th generation of Tom's family tree (don't count the Aa Bb mates at each
# level). Assume that Mendel's second law holds for the factors.

from scipy.special import binom


def ia_prob(k, N):
    """Compute the probability of finding N As/Bb alleles at step k."""
    def P(n, k):
        return binom(2**k, n) * 0.25**n * 0.75**(2**k - n)
    return 1 - sum(P(n, k) for n in range(N))


round(ia_prob(7, 35), 3)
