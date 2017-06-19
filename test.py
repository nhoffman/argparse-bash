#!/usr/bin/env python

"""Test output of various incantations of example.sh

"""

import unittest
from subprocess import check_output
from textwrap import dedent


def run(*args):
    return check_output(['./example.sh'] + list(args),
                        universal_newlines=True).strip()


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
        self.assertIn('arg with multiple values: [one fish] [two fish]', output)

    def test03(self):
        output = run('infile', 'outfile', '-d')
        self.assertIn('yes, do it', output)

    def test04(self):
        output = run('infile', 'outfile', '-a', '0')
        self.assertIn('the answer: 0', output)


if __name__ == '__main__':
    unittest.main()
