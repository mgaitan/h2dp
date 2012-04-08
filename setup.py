#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


with open('README.rst') as readme:
    __doc__ = readme.read()


setup(
    name = 'h2dp',
    version = '0.1',
    description = 'Hamster to dotProject logs sync tool',
    long_description = long_description,
    author = u'Martín Gaitán',
    author_email = 'gaitan@gmail.com',
    url='https://github.com/nqnwebs/h2dp',
    packages = ['h2dp',],
    license = 'GNU GENERAL PUBLIC LICENCE v3.0',
    install_requires = ['distribute', 'django', 'mechanize'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
    scripts = ['scripts/h2dp'],
)
