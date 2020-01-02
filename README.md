# splitseq
split fasta or other multi sequence files into individual sequence files. If
not input file is given it reads from the standard input. One output file is
created per sequence entry, using the sequence id and the corresponding format
to create the file name. Name uniqueness is enforced adding `_` to the output
file names, if necessary, to avoid overwriting.

## Usage
`splitseq [-h] [-f {fasta,clustal,embl,genbank,imgt,phd,pir,tab}] [-v]
                [multiseqfile]`

## Options
`
positional arguments:
  multiseqfile          Input multi-sequence file [default: stdin].

optional arguments:
  -h, --help            show this help message and exit
  -f {fasta,clustal,embl,genbank,imgt,phd,pir,tab}, --format {fasta,clustal,embl,genbank,imgt,phd,pir,tab}
                        Sequence format [default: fasta].
  -v, --version         Show program's version number and exit.
`

## Dependencies
* Python3
* Biopython
* argparse

