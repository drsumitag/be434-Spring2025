#!/usr/bin/env python3
"""
Author : Sumit Agarwal <drsumitag@arizona.edu>
Date   : 2025-04-23
Purpose: Sequence statistics for FASTA files
"""

import argparse
import os
import sys
from statistics import mean
from tabulate import tabulate


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Sequence statistics for FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        nargs='+',
                        help='Input FASTA file(s)')

    parser.add_argument('-t',
                        '--tablefmt',
                        help='Table format',
                        metavar='FORMAT',
                        default='plain',)

    return parser.parse_args()


def parse_fasta(filename):
    """Parse FASTA file, return list of sequence lengths"""
    lengths = []
    current_seq = ''

    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line.startswith('>'):
                    if current_seq:  # Save the previous seq before starting a new one
                        lengths.append(len(current_seq))
                        current_seq = ''
                else:
                    current_seq += line

            # Don't forget the last sequence
            if current_seq:
                lengths.append(len(current_seq))
    except FileNotFoundError:
        return []  # Return empty if file not found

    return lengths


def process_file(filename):
    """Process a FASTA file and return statistics"""
    lengths = parse_fasta(filename)
    num_seqs = len(lengths)

    if num_seqs > 0:
        min_len = min(lengths)
        max_len = max(lengths)
        avg_len = float(mean(lengths))  # Keep as float for formatting
        if avg_len == int(avg_len):
            avg_len += 0.00001
    else:
        min_len = max_len = avg_len = 0.0

    return {
        'name': os.path.relpath(filename),
        'min_len': min_len,
        'max_len': max_len,
        'avg_len': avg_len,
        'num_seqs': num_seqs
    }


def main():
    """Main function"""
    if len(sys.argv) == 1:  # No arguments provided
        parser = argparse.ArgumentParser(
            description='Sequence statistics for FASTA files',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.print_usage()
        sys.exit(1)

    args = get_args()
    table_format = args.tablefmt
    results = []

    # Process all provided files
    for file_path in args.FILE:
        # Directly check if the file exists
        if not os.path.isfile(file_path):
            # Print a more specific error message with the file path
            print(f"No such file or directory: '{file_path}'", file=sys.stderr)
            sys.exit(1)

        results.append(process_file(file_path))

    # Prepare data for tabulate with custom formatting
    headers = ['name', 'min_len', 'max_len', 'avg_len', 'num_seqs']

    # Apply custom float formatting to ensure decimal display
    formatted_data = []
    for r in results:
        formatted_data.append([
            r['name'],
            r['min_len'],
            r['max_len'],
            r['avg_len'],  # Format to always show 2 decimal places
            r['num_seqs']
        ])

    # Print the table using tabulate with floatfmt option
    if formatted_data:
        print(tabulate(
            formatted_data,
            headers=headers,
            tablefmt=table_format,
            floatfmt=".2f")
        )


if __name__ == '__main__':
    main()