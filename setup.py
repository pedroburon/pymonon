#!/usr/bin/env python
# encoding=UTF-8

from setuptools import setup

try:
    import multiprocessing
except ImportError:
    pass


setup(name='pymonon',
      version=__import__('pymonon').__version__,
      description='Python Money Helper',
      author=u'Pedro Burón',
      author_email='pedroburonv@gmail.com',
      url='http://pedroburon.info',
      test_suite='nose.collector',
      packages=['pymonon'],
      tests_require=['nose'],
      setup_requires=['distribute'],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Programming Language :: Python :: 2 :: Only',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Office/Business :: Financial :: Accounting',
      ]
      )
