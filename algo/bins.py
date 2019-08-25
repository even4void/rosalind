#!/usr/bin/env python3


def bins(lst, start, end, elt):
    """Binary search assuming lst is sorted (recursive version)."""
    mid = (start + end) // 2
    if start > end:
        return -1
    if elt == lst[mid]:
        # simulate 1-based indexing
        return mid+1
    elif elt < lst[mid]:
        return bins(lst, start, mid-1, elt)
    else:
        # elt < lst[mid]
        return bins(lst, mid+1, end, elt)


# See bins.txt for real test data
array = [10, 20, 30, 40, 50]
idx = [40, 10, 35, 15, 40, 20]

print([bins(array, 0, len(array)-1, x) for x in idx])
