#!/usr/bin/env python3
"""
Author : Sumit Agarwal <drsumitag@arizona.edu>
Date   : 2025-03-20
Purpose: Create synthetic sequences
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
                    description='Create synthetic sequences',
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-o",
                        "--outfile",
                        type=str,
                        default="out.fa",
                        help="Output filename")

    parser.add_argument("-t",
                        "--seqtype",
                        type=str,
                        default="dna",
                        help="DNA or RNA")

    parser.add_argument("-n",
                        "--numseqs",
                        type=int,
                        default=10,
                        help="Number of sequences to create")

    parser.add_argument("-m",
                        "--minlen",
                        type=int,
                        default=50,
                        help="Minimum length")

    parser.add_argument("-x",
                        "--maxlen",
                        type=int,
                        default=75,
                        help="Maximum length")

    parser.add_argument("-p",
                        "--pctgc",
                        type=float,
                        default=0.5,
                        help="Percentage GC")

    parser.add_argument("-s",
                        "--seed",
                        type=int,
                        default=None,
                        help="Random seed")

    args = parser.parse_args()

    # Verify pctgc
    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    # Verify seqtype
    if args.seqtype not in ["dna", "rna"]:
        parser.error(
                    f'--seqtype "{args.seqtype}" is invalid. '
                    'Must be "dna" or "rna"'
        )

    return parser.parse_args()


def create_pool(pctgc, max_len, seq_type):
    """ Create the pool of bases """

    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    with open(args.outfile, 'wt') as outfile:
        for i in range(args.numseqs):
            seq_len = random.randint(args.minlen, args.maxlen)
            sequence = ''.join(random.sample(pool, seq_len))
            outfile.write(f">{i + 1}\n{sequence}\n")

    print(
                    f'Done, wrote {args.numseqs} {args.seqtype.upper()}'
                    f' sequences to "{args.outfile}".'
    )


# --------------------------------------------------
if __name__ == '__main__':
    main()
