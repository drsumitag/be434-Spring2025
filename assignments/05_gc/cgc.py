#!/usr/bin/env python3
"""
Author : Sumit Agarwal <drsumitag@arizona.edu>
Date   : 2025-02-27
Purpose: Finding GC content in sequences
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='FILE',
                        help='Input sequence file',
                        nargs='?',
                        type=argparse.FileType('rt'),
                        default=sys.stdin)

    return parser.parse_args()


def calculate_gc_count(dna):
    """Compute GC content"""
    gc_count = dna.count('G') + dna.count('C')
    tot_count = len(dna)
    return (gc_count / tot_count)*100


def parse_fasta(file_handle):
    """Parses a FASTA file"""
    sequences = {}
    seq_id = None
    seq = ''
    try:
        for line in file_handle:
            line = line.strip()
            if line.startswith('>'):
                if seq_id:
                    sequences[seq_id] = seq
                seq_id = line[1:]
                seq = ''
            else:
                seq += line
        if seq_id:
            sequences[seq_id] = seq
        return sequences
    except (IOError, UnicodeDecodeError) as e:
        print(f"Error parsing FASTA: {e}")
        return {}


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    try:
        sequences = parse_fasta(args.positional)
        highest_gc = -1
        highest_id = None

        for seq_id, seq in sequences.items():
            current_gc = calculate_gc_count(seq)
            if current_gc > highest_gc:
                highest_gc = current_gc
                highest_id = seq_id

        if highest_id is not None:
            print(f'{highest_id} {highest_gc:.6f}')

    except (FileNotFoundError, IOError, UnicodeDecodeError) as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(2)


# --------------------------------------------------
if __name__ == '__main__':
    main()
