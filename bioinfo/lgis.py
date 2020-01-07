#!/usr/bin/env python3

# NOTE: See also
# - https://stackoverflow.com/q/3992697


def lseq(n, seq, op):
    """ mattdoug604/Rosalind """
    q = [0] * n
    p = [-1] * n

    for i in range(n):
        maxLen = 0
        for j in range(i):
            if op == '>':
                check = seq[i] > seq[j]
            elif op == '<':
                check = seq[i] < seq[j]
            if check is True:
                if q[j] > maxLen:
                    maxLen = q[j]
                    p[i] = j

        q[i] = maxLen + 1

    idx = q.index(max(q))
    ls = []
    while(idx != -1):
        ls = [seq[idx]] + ls
        idx = p[idx]

    return ls


lst = open("lgis.txt").readlines()
n, p = [x.strip() for x in lst]
n = int(n)
p = [int(i) for i in p.split()]

incr = lseq(n, p, '>')
decr = lseq(n, p, '<')

print("%s\n%s" % (" ".join(map(str, incr)), " ".join(map(str, decr))))
