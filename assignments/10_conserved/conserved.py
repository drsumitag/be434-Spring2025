#!/usr/bin/env python3
"""
Author : Sumit Agarwal <drsumitag@arizona.edu>
Date   : 2025-04-08
Purpose: Find conserved bases
"""


import argparse
import sys
import os

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('FILE',
                        metavar='FILE',
                        help='Input file')
    return parser.parse_args()

# --------------------------------------------------


def parse_fasta(file_path):
    """Parse a FASTA file and return sequences"""
    sequences = []
    headers = []
    current_seq = ""
    current_header = ""
    # Check if file exists before trying to open it
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file or directory: '{file_path}'")

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_seq:  # Save the previous sequence if it exists
                    sequences.append(current_seq)
                    headers.append(current_header)
                current_header = line[1:]  # Remove the '>' character
                current_seq = ""
            else:
                current_seq += line
                # Add the last sequence
        if current_seq:
            sequences.append(current_seq)
            headers.append(current_header)
            return sequences, headers

# --------------------------------------------------


def find_conserved(sequences):
    """Finds conserved bases in a list of sequences."""
    if not sequences:
        return ""
    num_sequences = len(sequences)
    sequence_length = len(sequences[0])
    conserved_line = ""
    for i in range(sequence_length):
        base = sequences[0][i]
        is_conserved = True
        for j in range(1, num_sequences):
            if i >= len(sequences[j]) or sequences[j][i] != base:
                is_conserved = False
                break
        if is_conserved:
            conserved_line += "|"  # Use '|' for conserved
        else:
            conserved_line += "X"  # Use 'X' for non-conserved
    return conserved_line

# --------------------------------------------------


if __name__ == '__main__':
    args = get_args()
    try:
        sequences, headers = parse_fasta(args.FILE)
        if not sequences:
            print("Error: No sequences found in the input file.")
            sys.exit(1)
        else:
            if not all(len(seq) == len(sequences[0]) for seq in sequences):
                print("Error:Input must be same length for simple comparison.")
                sys.exit(1)
            else:
                conserved_result = find_conserved(sequences)
                for seq_str in sequences:
                    print(seq_str)
                print(conserved_result)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
