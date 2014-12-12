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
