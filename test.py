#!/usr/bin/env python

"""Test output of various incantations of example.sh

"""

import unittest
import subprocess
from textwrap import dedent


def run(script,*args,expect_exit_1=False):
    cmd = [script] + list(args)
    if hasattr(subprocess, 'check_output'):
        # python 2.7+
        try:
            output = subprocess.check_output(cmd, universal_newlines=True).strip()
        except subprocess.CalledProcessError as cpe:
            if not expect_exit_1:
                raise cpe
            if cpe.returncode  != 1:
                raise cpe
            output = cpe.output 
    else:
        # python 2.6
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0].strip()
    return output


def strip(val):
    return dedent(val).strip()


class TestEverything(unittest.TestCase):

    def test01(self):
        output = run('./example.sh', 'infile', 'outfile')

        expected = strip("""
        required infile: infile
        required outfile: outfile
        the answer: 42
        do the thing? no, do not do it
        arg with multiple values: []
        """)

        self.assertEqual(output, expected)

    def test02(self):
        output = run('./example.sh', 'infile', 'outfile', '-m', 'one fish', 'two fish')
        self.assertTrue('arg with multiple values: [one fish] [two fish]' in output)

    def test03(self):
        output = run('./example.sh', 'infile', 'outfile', '-d')
        self.assertTrue('yes, do it' in output)

    def test04(self):
        output = run('./example.sh', 'infile', 'outfile', '-a', '0')
        self.assertTrue('the answer: 0' in output)

    def test05(self):
        # argparse.bash prints a script template
        output = run('./argparse.bash')
        self.assertTrue(output.startswith('#!/usr/bin/env bash'))

    def test06(self):
        output = run('./example.sh','-h', expect_exit_1 = True )
        self.assertTrue('epilog' in output)

if __name__ == '__main__':
    unittest.main()
