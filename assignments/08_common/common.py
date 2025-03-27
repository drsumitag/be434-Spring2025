#!/usr/bin/env python3
"""
Author : Sumit Agarwal <drsumitag@arizona.edu>
Date   : 2025-03-27
Purpose: Find common words
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find Common Words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input File 1')

    parser.add_argument('FILE2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input File 2')

    parser.add_argument('-o', '--outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout,
                        help='Output file (default: <stdout>)')

    return parser.parse_args()

# --------------------------------------------------


def main():
    """Main function to read two files and compare words"""

    args = get_args()

    # Read and process the contents of the two input files
    file1_words = set(args.FILE1.read().split())
    file2_words = set(args.FILE2.read().split())

    # Find the common words between both sets
    common_words = file1_words.intersection(file2_words)

    # Convert the set of common words to a sorted list for consistent order
    common_words = sorted(common_words)

    # If there are common words, print/write them
    if common_words:
        result = "\n".join(common_words) + "\n"
        if args.outfile != sys.stdout:
            args.outfile.write(result)  # Write to output file
        else:
            print(result)  # Print to stdout
    else:
        # If no common words, print a message or leave the output empty
        print("No common words found.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
