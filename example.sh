#!/usr/bin/env bash

ARGPARSE_DESCRIPTION="Sample script description"      # this is optional
ARGPARSE_EPILOG="This is the epilog."      # this is optional
# shellcheck source=/Users/aberezin/apps/argparse.bash
source "$ARGPARSE_PATH" || exit 1
#optional way to plave src file:  source $(dirname $0)/argparse.bash || exit 1
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
echo -n "do the thing?"
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

