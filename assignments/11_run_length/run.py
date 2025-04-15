#!/usr/bin/env python3
"""
Author : Sumit Agarwal <drsumitag@arizona.edu>
Date   : 2025-04-15
Purpose: Run length encoding of DNA
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='STR_OR_FILE',
                        help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------
def run_length_encode(text):
    """Performs run-length encoding on a string."""
    if not text:
        return ""

    encoded = []
    count = 1
    prev_char = text[0]

    for char in text[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded.append(prev_char)
            if count > 1:
                encoded.append(str(count))
            prev_char = char
            count = 1

    encoded.append(prev_char)
    if count > 1:
        encoded.append(str(count))

    return "".join(encoded)

# --------------------------------------------------


def main():
    """The main function - performs run-length encoding"""

    args = get_args()
    input_arg = args.input

    if os.path.isfile(input_arg):
        try:
            with open(input_arg, 'r') as file_handle:
                input_text = file_handle.read().strip()
        except IOError:
            print(f"Error:Could not read file'{input_arg}'", file=sys.stderr)
            sys.exit(1)
    else:
        input_text = input_arg

    if not input_text:
        print("Error: No input provided.", file=sys.stderr)
        sys.exit(1)

    encoded_text = run_length_encode(input_text)
    print(encoded_text)

# --------------------------------------------------


if __name__ == '__main__':
    main()
