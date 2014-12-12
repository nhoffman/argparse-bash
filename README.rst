===============
 argparse.bash
===============

Use python's argparse module in shell scripts

The function `argparse` parses its arguments using
argparse.ArgumentParser; the parser is defined in the function's
stdin. Here's the contents of ``example.sh``; ``argparse.bash`` needs
to be in the same directory)::

  #!/bin/bash

  source $(dirname $0)/argparse.bash
  argparse "$@" <<EOF || exit 1
  parser.add_argument('infile')
  parser.add_argument('outfile')
  parser.add_argument('-n', '--not-required', default=42, type=int,
                      help='optional argument [default %(default)s]')
  EOF

  echo required infile: "$INFILE"
  echo required outfile: "$OUTFILE"
  echo optional: "$NOT_REQUIRED"


Help text looks like this::

  $ ./example.sh -h
  usage: example.sh [-h] [-n NOT_REQUIRED] infile outfile

  positional arguments:
    infile
    outfile

  optional arguments:
    -h, --help            show this help message and exit
    -n NOT_REQUIRED, --not-required NOT_REQUIRED
			  optional argument [default 42]


Error message (both infile and outfile are required)::

  $ ./example.sh foo
  usage: example.sh [-h] [-n NOT_REQUIRED] infile outfile
  example.sh: error: too few arguments


Example output of this script::

  $ ./example.sh infile.txt "name with spaces.txt"
  required infile: infile.txt
  required outfile: name with spaces.txt
  optional: 42


Executing ``argparse.bash`` (as opposed to sourcing it) prints a
script template, so that you can start a new script like this::

  $ argparse.bash > my_script_using_argparse.sh
