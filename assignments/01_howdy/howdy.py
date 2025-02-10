#!/usr/bin/env python3
"""
Author : Sumit Agarwal
Purpose: 'Print greeting'
"""
import argparse


# --------------------------------------------------
def get_args():
    """Get arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        type=str,
                        default='Howdy',
                        help='The greeting')

    parser.add_argument('-n',
                        '--name',
                        type=str,
                        default='Stranger',
                        help='Whom to greet')

    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """Greetings"""

    args = get_args()

    if args.excited:
        print(f'{args.greeting}, {args.name}!')
    else:
        print(f'{args.greeting}, {args.name}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
