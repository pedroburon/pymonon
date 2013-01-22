#!/usr/bin/env python
# encoding=UTF-8

from distribute_setup import use_setuptools
use_setuptools()

try:
    import multiprocessing
except ImportError:
    pass

from setuptools import setup

from pymonon import __version__


setup(name='pymonon',
      version=__version__,
      description='Python Money Helper',
      author=u'Pedro Burón',
      author_email='pedroburonv@gmail.com',
      url='http://pedroburon.info',
      test_suite='nose.collector',
      packages=['pymonon'],
      tests_require=['nose']
     )
