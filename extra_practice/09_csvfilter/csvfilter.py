#!/usr/bin/env python3
"""
Author : Sumit Agarwal <drsumitag@arizona.edu>
Date   : 2025-04-01
Purpose: Filter a delimited text file for some value
"""

import argparse
import csv 
import re
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""



     # First, check if -f/--file is present and exists before regular parsing
    file_arg = None
    for i, arg in enumerate(sys.argv):
        if arg in ['-f', '--file'] and i + 1 < len(sys.argv):
            file_arg = sys.argv[i + 1]
            if file_arg.startswith('-'):
                file_arg = None
            break
    
    # If file arg was found, check if it exists
    if file_arg and not os.path.isfile(file_arg):
        print(f"No such file or directory: '{file_arg}'", file=sys.stderr)
        sys.exit(1)
        

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        required=True,
                        help='Input file')

    parser.add_argument('-v',
                        '--val',
                        required=True,
                        metavar='val',
                        help='Value for filter')

    parser.add_argument('-c',
                        '--col',
                        metavar='col',
                        help='column name for filter')
                        #default="")

    parser.add_argument('-o',
                        '--outfile',
                        metavar='OUTFILE',
                        help='Output filename (default: out.csv)',
                        default="out.csv")

    parser.add_argument('-d',
                        '--delim',
                        '--delimiter',
                        dest='delim',
                        metavar='delim',
                        help='Input delimiter (default: ,)',
                        default=',')


    
    return parser.parse_args()

# --------------------------------------------------

def main():
    """Make a jazz noise here"""
    args = get_args()
    file_arg = args.file               # Input file
    val_arg = args.val                 # Value to search
    col_arg = args.col                 # Optional column
    outfile_arg = args.outfile         # Output file name
    
    if args.delim in ['\\t',r'\t','\t','t']:
        delim_arg = '\t'  # Convert string '\t' to actual tab character
    else:
        delim_arg = args.delim
    
    try:
        # Open the input CSV file
        with open(file_arg, mode='r', newline='', encoding='utf-8') as infile:
            # Create a CSV reader
            reader = csv.DictReader(infile, delimiter=delim_arg)
            
            # Get fieldnames before consuming the reader
            fieldnames = reader.fieldnames

            # Check if the column exists when specified
            if col_arg and col_arg not in fieldnames:
                print(f'--col "{col_arg}" not a valid column! ' +
                      f'Choose from {", ".join(fieldnames)}', 
                      file=sys.stderr)
                sys.exit(1)

            # Filter rows based on the value and column
            filtered_rows = []
            for row in reader:
                # If column is specified, filter by column
                if col_arg:
                    if re.search(val_arg, str(row[col_arg]), re.IGNORECASE):
                        filtered_rows.append(row)
                else:
                    # If no column is specified, filter by value in any field
                    if any(re.search(val_arg, str(cell), re.IGNORECASE) for cell in row.values()):
                        filtered_rows.append(row)
            
        # Open the output CSV file to write the filtered results
        with open(outfile_arg, mode='w', newline='', encoding='utf-8') as outfile:
            # Create a CSV writer
            writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=delim_arg)
            #writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames) writer.writeheader()
            
            # Write the header
            writer.writeheader()
            
            # Write the filtered rows
            writer.writerows(filtered_rows)
            
        # Output the number of rows written to the output file
        print(f'Done, wrote {len(filtered_rows)} to "{outfile_arg}".')
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

  
# --------------------------------------------------
if __name__ == '__main__':
    main()