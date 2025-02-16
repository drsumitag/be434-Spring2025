#!/usr/bin/env python3
"""
Author : Sumit Agarwal <drsumitag@arizona.edu>
Date   : 2025-02-15
Purpose: Create python program dna.py
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        help='Input DNA sequence',
                        metavar='DNA',
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    dna_cnt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for base in args.positional:
        if base in dna_cnt:
            dna_cnt[base] += 1

    print(dna_cnt['A'], dna_cnt['C'], dna_cnt['G'], dna_cnt['T'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
