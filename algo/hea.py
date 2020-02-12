#!/usr/bin/env python3


def max_heap(lst):
    """
    >>> a = [1, 3, 5, 7, 2]
    >>> max_heap(a)
    >>> print(" ".join(map(str, a)))
    7 5 1 3 2
    """
    def swap(lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]
        return lst

    for i in range(len(lst) - 1, 0, -1):
        parent = (i - 1) // 2
        if lst[i] > lst[parent]:
            lst = swap(lst, parent, i)
            v = i
            while True:
                max_node = v
                if v * 2 + 1 < len(lst) and lst[v * 2 + 1] > lst[max_node]:
                    max_node = v * 2 + 1
                if v * 2 + 2 < len(lst) and lst[v * 2 + 2] > lst[max_node]:
                    max_node = v * 2 + 2
                if max_node == v:
                    break
                lst = swap(lst, v, max_node)
                v = max_node


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open("hea.txt") as f:
        next(f)
        for line in f:
            items = list(map(int, line.strip().split()))
    f.close()

    max_heap(items)
    print(" ".join(map(str, items)))
