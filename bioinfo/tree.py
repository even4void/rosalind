#!/usr/bin/env python3

tr = open("tree.txt").readlines()
n = int(tr[0].strip())
print(n - len(tr))
