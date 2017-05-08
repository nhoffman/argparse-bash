#!/bin/bash

source $(dirname $0)/argparse.bash || exit 1
argparse "$@" <<EOF || exit 1
parser.add_argument('infile')
parser.add_argument('outfile')
parser.add_argument('-n', '--not-required', nargs='+',
                    help='optional multi value argument [default %(default)s]')
EOF

echo required infile: "$INFILE"
echo required outfile: "$OUTFILE"
echo optional: 
for a in "${NOT_REQUIRED[@]}"
do
    echo "  $a"
done