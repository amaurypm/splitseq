#!/usr/bin/env python3
## Split fasta or other multi sequence files into individual sequence files. 
##
## Amaury Pupo Merino
## amaury.pupo@gmail.com
##
## This script is released under GPL v3.
##

## Importing modules
import argparse
import sys
import os
from Bio import SeqIO

## Functions

## Main
def main():
    """Main function.
    """
    parser=argparse.ArgumentParser(description="Split fasta or other multi sequence files into individual sequence files. If not input file is given it reads from the standard input. One output file is created per sequence entry, using the sequence id and the corresponding format to create the file name. Name uniqueness is enforced adding '_' to the output file names, if necessary, to avoid overwriting.")
    parser.add_argument('multiseqfile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Input multi-sequence file [default: stdin].')
    #parser.add_argument('outseqfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='Output sequence file [default: stdout].')
    parser.add_argument('-f', '--format', choices=['fasta','clustal', 'embl', 'genbank', 'imgt', 'phd', 'pir', 'tab'], default='fasta', help='Sequence format [default: %(default)s].')
    parser.add_argument('-v', '--version', action='version', version='0.1.0', help="Show program's version number and exit.")

    args=parser.parse_args()

    try:
        for record in SeqIO.parse(args.multiseqfile, args.format):
            output_filename = record.id + '.' + args.format
            while(os.path.isfile(output_filename)):
                output_filename = os.path.splitext(output_filename)[0] + '_' + '.' + args.format

            SeqIO.write(record, output_filename, args.format)
            

    except ValueError:
        sys.stderr.write("ERROR: Input has not a valid {} format.".format(args.format))
        sys.exit(1)


## Running the script
if __name__ == "__main__":
        main()

