#!/usr/bin/env python3
"""
Author : Sumit Agarwal <drsumitag@arizona.edu>
Date   : 2025-02-06
Purpose: Python program that will divide two required integer values
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Divide two numbers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "INT", metavar="INT", nargs=2, type=int, help="Numbers to divide"
    )

    args = parser.parse_args()

    # Handle division by zero here
    if args.INT[1] == 0:
        parser.error("Cannot divide by zero, dum-dum!")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Divide Integers"""

    args = get_args()
    convert_str = [str(i) for i in args.INT]
    div_str = " / ".join(convert_str)

    print(f"{div_str} = {args.INT[0] // args.INT[1]}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
