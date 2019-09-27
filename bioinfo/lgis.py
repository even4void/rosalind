#!/usr/bin/env python3

# NOTE: See also
# - https://stackoverflow.com/q/3992697
# - https://www.algorithmist.com/index.php/Longest_Increasing_Subsequence


def lis(xs):
    """Rosetta code: https://is.gd/IZbn7I."""
    N = len(xs)
    P = [0] * N
    M = [0] * (N + 1)
    L = 0
    for i in range(N):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if xs[M[mid]] < xs[i]:
                lo = mid + 1
            else:
                hi = mid - 1
        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i
        if newL > L:
            L = newL
    S = []
    k = M[L]
    for i in range(L - 1, -1, -1):
        S.append(xs[k])
        k = P[k]
    return S[::-1]


lst = open("lgis.txt").readlines()
n, p = [x.strip() for x in lst]
p = p.split()

incr = lis(p)
decr = lis(p[::-1])[::-1]

print("%s\n%s" % (" ".join(incr), " ".join(decr)))
