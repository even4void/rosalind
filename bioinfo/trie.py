#!/usr/bin/env python3

# See also:
# - http://adijo.github.io/2016/01/21/rosalind-introduction-to-pattern-matching/
# - https://github.com/bdimmick/python-trie

from itertools import count

DEBUG = True


class Trie:
    """A simple trie implementation"""

    def __init__(self):
        self.counter = count(start=1)
        self.root = [next(self.counter), {}]

    def insert(self, sequence):
        node = self.root
        for ch in sequence:
            if ch not in node[1]:
                node[1][ch] = [next(self.counter), {}]
            node = node[1][ch]


with open("trie.txt") as fh:
    data = fh.readlines()

ss = [line.strip() for line in data]
tt = Trie()
for s in ss:
    tt.insert(s)

if DEBUG:
    print(tt.root)
