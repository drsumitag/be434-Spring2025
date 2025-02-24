#!/usr/bin/env python3
"""
Author : Sumit Agarwal <drsumitag@arizona.edu>
Date   : 2025-02-23
Purpose: Reverse Complement DNA
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        help='Input DNA sequence',
                        metavar='DNA',
                        )

    return parser.parse_args()


def rev_comp(dna):
    """Compute the reverse complement of a DNA sequence"""
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
            'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    return ''.join(comp[base] for base in reversed(dna))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if os.path.isfile(args.positional):
        try:
            with open(args.positional, encoding='utf-8') as f:
                dna_sequence = f.read().strip()
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return

    else:
        dna_sequence = args.positional

    print(rev_comp(dna_sequence))


# --------------------------------------------------
if __name__ == '__main__':
    main()
