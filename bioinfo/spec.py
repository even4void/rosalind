#!/usr/bin/env python3


MASS = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}


def _nearest(w):
    """Finds closest amino acid based on weight."""
    return min(MASS.items(), key=lambda x: abs(x[1] - w))[0]


def prefix_spectrum(w):
    diffs = [i - j for j, i in zip(w, w[1:])]
    return "".join([_nearest(w) for w in diffs])


# sample = [3524.8542, 3710.9335, 3841.974, 3970.0326, 4057.0646]
# print(prefix_spectrum(sample))

with open("spec.txt", "r") as f:
    weights = [float(n) for n in f.read().strip().split('\n')]
    print(prefix_spectrum(weights))
