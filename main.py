

import argparse
import os
from typing import NamedTuple

class Args(NamedTuple):
    dna: str

def get_args() -> Args:
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(description='Tetranucleotide frequency',formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', metavar='DNA', help='Input DNA sequence')
    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()
    return Args(args.dna)

def countIt() -> None:
    args = get_args()
    a_count, c_count, g_count, t_count = 0, 0, 0, 0

    print(args.dna)

    for base in args.dna:
        if base == 'A':
            a_count += 1
        elif base == 'C':
            c_count += 1
        elif base == 'G':
            g_count += 1
        elif base == 'T':
            t_count += 1

    print(a_count, c_count, g_count, t_count)

if __name__ == '__main__':
    countIt()

