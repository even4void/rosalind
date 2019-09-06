#!/usr/bin/env python3


def translate(seq):
    """codon->protein"""
    codons = {'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
              'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
              'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
              'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
              'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
              'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
              'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
              'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
              'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
              'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
              'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
              'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
              'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
              'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
              'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
              'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'}
    if len(seq) == 3 and seq in codons:
        return codons[seq]
    else:
        return None


def reverse(seq):
    "reverse complement"
    nucl = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return "".join([nucl[x] for x in reversed(seq)])


def lookup(seq):
    res = []
    iloc = []

    # find start codon (ATG -> M)
    for i in range(len(seq)):
        prot = translate(seq[i:i+3])
        if prot and prot == 'M':
            iloc.append(i)

    # iterate over all matches
    for i in iloc:
        stop = False
        found = ''
        for j in range(i, len(seq), 3):
            prot = translate(seq[j:j+3])
            if not prot or prot == 'Stop':
                stop = True
                break
            found += prot
        if stop:
            res.append(found)

    return res


def lookup_all(seq):
    """
    >>> s = '''AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGA
        TTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'''
    >>> print(" ".join(lookup_all(s.replace("\n", ""))))
    M MLLGSFRLIPKETLIQVAGSSPCNLS MTPRLGLESLLE MGMTPRLGLESLLE
    """
    fw = lookup(seq)
    bw = lookup(reverse(seq))
    return set(fw + bw)


if __name__ == '__main__':
    with open('orf.txt') as f:
        next(f)
        s = [line.rstrip().split() for line in f]

    seq = "".join(["".join(x) for x in s])
    print(" ".join(lookup_all(seq)))
