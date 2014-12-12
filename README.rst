===============
 argparse.bash
===============

Use python's argparse module in shell scripts

The function ``argparse`` parses its arguments using
``argparse.ArgumentParser`` The parser is defined in the function's
stdin. ``argparse.bash`` should be in the same directory as a script
that uses it.

Python 2.7 is required. See
https://docs.python.org/2.7/library/argparse.html for a description of
the python module.

Installation
============

Get ``argparse.sh``::

  wget https://raw.githubusercontent.com/nhoffman/argparse-bash/master/argparse.bash
  chmod +x argparse.bash

Then move the file into the same directory as any scripts that will use it.

Usage
=====

Here's an example, ``example.sh``::

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


Example output of this script::

  $ ./example.sh infile.txt "name with spaces.txt"
  required infile: infile.txt
  required outfile: name with spaces.txt
  optional: 42


Note that hyphens in the long option names are changed to underscores,
and variables are all-caps (to be more bash-y).

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


Executing ``argparse.bash`` (as opposed to sourcing it) prints a
script template, so that you can start a new script like this::

  $ argparse.bash > my_script_using_argparse.sh
