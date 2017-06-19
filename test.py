#!/usr/bin/env python

"""Test output of various incantations of example.sh

"""

import unittest
import subprocess
from textwrap import dedent


def run(*args):
    cmd = ['./example.sh'] + list(args)
    if hasattr(subprocess, 'check_output'):
        # python 2.7+
        output = subprocess.check_output(cmd, universal_newlines=True).strip()
    else:
        # python 2.6
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0].strip()

    return output


def strip(val):
    return dedent(val).strip()


class TestEverything(unittest.TestCase):

    def test01(self):
        output = run('infile', 'outfile')

        expected = strip("""
        required infile: infile
        required outfile: outfile
        the answer: 42
        do the thing? no, do not do it
        arg with multiple values: []
        """)

        self.assertEqual(output, expected)

    def test02(self):
        output = run('infile', 'outfile', '-m', 'one fish', 'two fish')
        self.assertTrue('arg with multiple values: [one fish] [two fish]' in output)

    def test03(self):
        output = run('infile', 'outfile', '-d')
        self.assertTrue('yes, do it' in output)

    def test04(self):
        output = run('infile', 'outfile', '-a', '0')
        self.assertTrue('the answer: 0' in output)


if __name__ == '__main__':
    unittest.main()
