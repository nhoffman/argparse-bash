===============
 argparse.bash
===============

Use Python's argparse module in shell scripts

.. image:: https://github.com/nhoffman/argparse-bash/actions/workflows/test.yml/badge.svg
   :target: https://github.com/nhoffman/argparse-bash/actions/workflows/test.yml

The function ``argparse`` parses its arguments using
``argparse.ArgumentParser``. The command line options are defined in
the function's stdin. ``argparse.bash`` should be in the same
directory as a script that uses it.

Python 2.7 or 3.5+ is required. See
https://docs.python.org/2.7/library/argparse.html for a description of
the python module. Note that some of the Python module's features
won't work as expected (or at all) in this simplistic implementation.


Installation
============

Get ``argparse.bash``

.. code-block:: shell

  wget https://raw.githubusercontent.com/nhoffman/argparse-bash/master/argparse.bash
  chmod +x argparse.bash

Then move the file into the same directory as any scripts that will use it.

Alternatively, you can paste the body of the ``argparse()`` function
into your script (in which case you would of course omit the line
sourcing ``argparse.bash`` in the examples below).


Usage
=====

Here's an example, ``example.sh``

.. code-block:: bash

  #!/usr/bin/env bash

  ARGPARSE_DESCRIPTION="Sample script description"      # this is optional
  source $(dirname $0)/argparse.bash || exit 1
  argparse "$@" <<EOF || exit 1
  parser.add_argument('infile')
  parser.add_argument('outfile')
  parser.add_argument('-a', '--the-answer', default=42, type=int,
		      help='Pick a number [default %(default)s]')
  parser.add_argument('-d', '--do-the-thing', action='store_true',
		      default=False, help='store a boolean [default %(default)s]')
  parser.add_argument('-m', '--multiple', nargs='+',
		      help='multiple values allowed')
  EOF

  echo required infile: "$INFILE"
  echo required outfile: "$OUTFILE"
  echo the answer: "$THE_ANSWER"
  echo -n do the thing?
  if [[ $DO_THE_THING ]]; then
      echo " yes, do it"
  else
      echo " no, do not do it"
  fi
  echo -n "arg with multiple values: "
  for a in "${MULTIPLE[@]}"; do
      echo -n "[$a] "
  done
  echo

Example output of this script::

  $ ./example.sh infile.txt "name with spaces.txt"
  required infile: infile.txt
  required outfile: name with spaces.txt
  the answer: 42
  do the thing? no, do not do it
  arg with multiple values: []

Note that hyphens in the long option names are changed to underscores,
and variables are all-caps (to be more bash-y).

Help text looks like this::

  $ ./example.sh -h
  usage: example.sh [-h] [-a THE_ANSWER] [-d] [-m MULTIPLE [MULTIPLE ...]]
		    infile outfile

  Sample script description

  positional arguments:
    infile
    outfile

  optional arguments:
    -h, --help            show this help message and exit
    -a THE_ANSWER, --the-answer THE_ANSWER
			  Pick a number [default 42]
    -d, --do-the-thing    store a boolean [default False]
    -m MULTIPLE [MULTIPLE ...], --multiple MULTIPLE [MULTIPLE ...]
			  multiple values allowed

Error messages::

  $ ./example.sh foo
  usage: example.sh [-h] [-a THE_ANSWER] [-d] [-m MULTIPLE [MULTIPLE ...]]
		    infile outfile
  example.sh: error: too few arguments
  $ ./example.sh foo bar -n baz
  usage: example.sh [-h] [-a THE_ANSWER] [-d] [-m MULTIPLE [MULTIPLE ...]]
		    infile outfile
  example.sh: error: unrecognized arguments: -n baz

Executing ``argparse.bash`` (as opposed to sourcing it) prints a
script template to stdout

.. code-block:: bash

  $ ./argparse.bash
  #!/usr/bin/env bash

  source $(dirname $0)/argparse.bash || exit 1
  argparse "$@" <<EOF || exit 1
  parser.add_argument('infile')
  parser.add_argument('-o', '--outfile')

  EOF

  echo "INFILE: ${INFILE}"
  echo "OUTFILE: ${OUTFILE}"

A few notes:

- ``action=store_true`` or ``store_false`` provides a value of "yes"
  for True, "" for False
- ``args='+'`` or ``args='*'`` provides an array of values.


License
=======

MIT License (see LICENSE.txt)

Copyright (c) 2017 - 2022 Noah Hoffman

