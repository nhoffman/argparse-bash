===============
 argparse.bash
===============

Use Python's argparse module in shell scripts

.. image:: https://travis-ci.org/nhoffman/argparse-bash.svg?branch=master
   :target: https://travis-ci.org/nhoffman/argparse-bash

The function ``argparse`` parses its arguments using
``argparse.ArgumentParser``. The command line options are defined in
the function's stdin. ``argparse.bash`` should be in the same
directory as a script that uses it.

Python 2.6+ or 3.2+ is required. See
https://docs.python.org/2.7/library/argparse.html for a description of
the python module. Note that some of the Python module's features (eg,
boolean values) aren't going to work as expected (or at all) in this
simplistic implementation.


Installation
============

Get ``argparse.bash``::

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

  source $(dirname $0)/argparse.bash || exit 1
  argparse "$@" <<EOF || exit 1
  parser.add_argument('infile')
  parser.add_argument('outfile')
  parser.add_argument('-a', '--the-answer', default=42, type=int,
		      help='Pick a number [default %(default)s]')
  parser.add_argument('-m', '--multiple', nargs='+',
		      help='multiple values allowed')
  EOF

  echo required infile: "$INFILE"
  echo required outfile: "$OUTFILE"
  echo the answer: "$THE_ANSWER"
  echo multiple:
  for a in "${MULTIPLE[@]}"; do
      echo "  $a"
  done

Example output of this script::

  $ ./example.sh infile.txt "name with spaces.txt"
  required infile: infile.txt
  required outfile: name with spaces.txt
  optional: 42


Note that hyphens in the long option names are changed to underscores,
and variables are all-caps (to be more bash-y).

Help text looks like this::

  $ ./example.sh -h
  usage: example.sh [-h] [-a THE_ANSWER] [-m MULTIPLE [MULTIPLE ...]]
		    infile outfile

  positional arguments:
    infile
    outfile

  optional arguments:
    -h, --help            show this help message and exit
    -a THE_ANSWER, --the-answer THE_ANSWER
			  Pick a number [default 42]
    -m MULTIPLE [MULTIPLE ...], --multiple MULTIPLE [MULTIPLE ...]
			  multiple values allowed

Error messages::

  $ ./example.sh foo
  usage: example.sh [-h] [-a THE_ANSWER] [-m MULTIPLE [MULTIPLE ...]]
		    infile outfile
  example.sh: error: too few arguments
  $ ./example.sh foo bar -n baz
  usage: example.sh [-h] [-a THE_ANSWER] [-m MULTIPLE [MULTIPLE ...]]
		    infile outfile
  example.sh: error: unrecognized arguments: -n baz

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

License
=======

MIT License (see LICENSE.txt)

Copyright (c) 2017 Noah Hoffman

