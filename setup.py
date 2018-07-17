#!/usr/bin/env python

import sys
from distutils.core import setup
from setuptools.command.test import test as TestCommand
from setuptools import setup, find_packages

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)

setup(name='nbayes',
    version       =  '1.0',
    description   =  'My boring Bayesian computer',
    author        =  'Paul Miller',
    author_email  = 'paul@jettero.pl',
    url           = 'https://github.com/jettero/trivial-bayes',
    tests_require = ['pytest'],
    packages      = find_packages(),
    cmdclass      = {'test': PyTest},
)

