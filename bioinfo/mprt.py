#!/usr/bin/env python3

import re
from Bio import ExPASy
from Bio import SeqIO

regex = re.compile('N[^P][ST][^P]')

with open("mprt.txt") as f:
    for line in f:
        h = ExPASy.get_sprot_raw(line.strip())
        s = SeqIO.read(h, "swiss")
        match = regex.finditer(str(s.seq))

        print(line.strip())
        for k in match:
            print(k.start()+1, end=" ")
        print()
