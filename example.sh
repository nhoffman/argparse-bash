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
