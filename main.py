import argparse
import os
import pathlib

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

# Counting DNA Nucleotides
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

# DNA to RNA converter
def dna_to_rna(dna_seq):
    return dna_seq.replace('T', 'U')

def read_input(filename):
    current_dir = pathlib.Path(__file__).parent
    with open(f'{current_dir}/' + filename) as fp:
        input_data = fp.read()
    return input_data

def get_compl_strand(dna_strand_1):
    dna_compliments = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}
    dna_strand_2 = ''
    n = len(dna_strand_1)
    for idx in range(n - 1, -1, -1):
        nuclio = dna_strand_1[idx]
        dna_strand_2 += dna_compliments[nuclio]
    return dna_strand_2

if __name__ == '__main__':
    # Counting DNA Nucleotides
    print('******* Counting the nucleotides in a DNA String *******')
    countIt()

    print('--------------------------------------------')

    # DNA to RNA
    print('********* Converting a DNA String to a RNA String ***********')
    in_data = read_input('prob_2_input.txt')
    print(dna_to_rna(in_data))

    # Compliment a DNA strand
    print('********* Determining the Reverse Compliment of a DNA String ***********')
    in_data = read_input('prob_3_input.txt')
    print(get_compl_strand(in_data))

