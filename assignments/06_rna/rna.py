#!/usr/bin/env python3
"""
Author : Sumit Agarwal <drsumitag@arizona.edu>
Date   : 2025-03-08
Purpose: Transcribe DNA into RNA
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribe DNA to RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='FILE',
                        help='Input DNA file',
                        nargs='*',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--out_dir',
                        help='Output directory',
                        metavar='DIR',
                        dest="outdir",
                        default='out')

    return parser.parse_args()


def transcribe_dna_to_rna(dna_sequence):
    """Transcribes a DNA sequence to RNA."""
    return dna_sequence.replace('T', 'U')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if not args.positional:
        print("usage: rna.py [-h] [-o DIR] FILE [FILE ...]")
        print("rna.py: error: no input files provided.")
        sys.exit(2)

    sequences_count = 0
    files_count = 0

    os.makedirs(args.outdir, exist_ok=True)

    for input_file in args.positional:
        if input_file is sys.stdin:
            output_filename = "stdin.txt"
        else:
            output_filename = os.path.splitext(
                os.path.basename(input_file.name)
            )[0] + ".txt"

        output_path = os.path.join(args.outdir, output_filename)

        try:
            with open(output_path, 'w', encoding='utf-8') as outfile:
                for line in input_file:
                    dna_sequence = line.strip()
                    rna_sequence = transcribe_dna_to_rna(dna_sequence)
                    outfile.write(rna_sequence + '\n')
                    sequences_count += 1  # Increment sequence count

            files_count += 1  # Increment file count

        except (IOError, UnicodeDecodeError) as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(2)

    sequence_str = "sequence" if sequences_count == 1 else "sequences"
    file_str = "file" if files_count == 1 else "files"

    print(f'Done, wrote {sequences_count} {sequence_str} in '
          f'{files_count} {file_str} to directory "{args.outdir}".', end="")


# --------------------------------------------------
if __name__ == '__main__':
    main()
