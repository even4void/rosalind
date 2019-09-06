#!/usr/bin/env python3

from itertools import product


def aslist(generator):
    "generator -> list"
    def wrapper(*args, **kwargs):
        return list(generator(*args, **kwargs))
    return wrapper


@aslist
def permutations(iterable, r=None):
    """From itertools, https://is.gd/Aw9JW0. Also https://is.gd/vYTGbT."""
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


def fmt(lst):
    out = [str(len(lst))]
    out.append("\n".join([" ".join(map(str, x)) for x in lst]))
    return "\n".join(out)


r = permutations(range(1, 6))
print(fmt(r))
