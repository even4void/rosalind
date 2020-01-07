
#!/usr/bin/env python3


def pair(seq):
    if len(seq) < 4:
        return 1
    if seq in prev:
        return prev[seq]
    else:
        prev[seq] = pair(seq[1:])
        for i in range(4, len(seq)):
            if seq[i] in match[seq[0]]:
                prev[seq] += pair(seq[1:i]) * pair(seq[i+1:])
    return prev[seq]


match = {'A':'U', 'U':'AG', 'C':'G', 'G':'CU'}
prev = {}

with open("rnas.txt", "r") as fh:
    seq = fh.read().replace("\n", "")
print(pair(seq))
