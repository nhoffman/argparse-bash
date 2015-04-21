===============
 argparse.bash
===============

Use Python's argparse module in shell scripts

The function ``argparse`` parses its arguments using
``argparse.ArgumentParser``. The command line options are defined in
the function's stdin. ``argparse.bash`` should be in the same
directory as a script that uses it.

Python 2.7+ or 3.2+ is required. See
https://docs.python.org/2.7/library/argparse.html for a description of
the python module. Note that some of the Python module's features (eg,
nargs='+', boolean values) aren't going to work well (or at all) in
this simplistic implementation.


Rationale
=========

There isn't a good one. This is an abomination, really. The proper
thing to do would be to abandon *sh altogether, and instead use a
scripting language with a proper library for defining a command line
interface. Can anyone think of one?


Installation
============

Get ``argparse.sh``::

  wget https://raw.githubusercontent.com/nhoffman/argparse-bash/master/argparse.bash
  chmod +x argparse.bash

Then move the file into the same directory as any scripts that will use it.

Alternatively, you can paste the body of the ``argparse()`` function
into your script (in which case you would of course omit the line
sourcing ``argparse.bash`` in the examples below).


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


Error messages::

  $ ./example.sh foo
  usage: example.sh [-h] [-n NOT_REQUIRED] infile outfile
  example.sh: error: too few arguments
  $ ./example.sh foo bar -n baz
  usage: example.sh [-h] [-n NOT_REQUIRED] infile outfile
  example.sh: error: argument -n/--not-required: invalid int value: 'baz'

Executing ``argparse.bash`` (as opposed to sourcing it) prints a
script template to stdout::

  $ ./argparse.bash
  #!/bin/bash

  source $(dirname $0)/argparse.bash || exit 1
  argparse "$@" <<EOF || exit 1
  parser.add_argument('infile')
  parser.add_argument('-o', '--outfile')
  EOF
  echo "INFILE: ${INFILE}"
  echo "OUTFILE: ${OUTFILE}"

