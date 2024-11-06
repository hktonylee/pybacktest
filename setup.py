#!/usr/bin/env python
# coding: utf8

VERSION = '0.1.1'

import sys

import setuptools
from setuptools import setup

setuptools_major_version = int(setuptools.__version__.split('.')[0])

extra_args = {}
if (sys.version_info[0] >= 3) and setuptools_major_version < 58:
    extra_args['use_2to3'] = True

setup(name='pybacktest',
      version=VERSION,
      description='pybacktest',
      author='Matvey Ezhov',
      url='https://github.com/ematvey/pybacktest',
      packages=['pybacktest'],
      install_requires=['numpy>=1.11',
                        'pandas>=0.19',
                        'pyyaml',
                        'cached_property'],
      **extra_args)
