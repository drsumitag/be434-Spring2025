#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Author : Sumit Agarwal <drsumitag@arizona.edu>
Date   : 2025-04-29
Purpose: Substitution Cipher
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Substitution cipher')

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-n',
                        '--number',
                        metavar='NUMBER',
                        type=int,
                        default=3,
                        help='A number to shift (default: 3)')

    parser.add_argument('-d',
                        '--decode',
                        action='store_true',
                        help='A boolean flag (default: False)')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        help='Output file (default: std.out)')
    args = parser.parse_args()

# If outfile is not provided, set it to stdout
    if not args.outfile:
        args.outfile = sys.stdout

    return args


# --------------------------------------------------



# --------------------------------------------------
def main():
    """Main function"""
    args = get_args()

    # Read the input text
    text = args.FILE.read().strip()

    # Apply the Caesar cipher
    result = caesar_cipher(text, args.number, args.decode)

    # Write the result to the output file
    args.outfile.write(result)

    # Add a newline if writing to stdout
    if args.outfile == sys.stdout:
        args.outfile.write('\n')

# --------------------------------------------------


if __name__ == '__main__':
    main()
