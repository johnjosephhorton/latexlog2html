#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os.path import join, dirname

import latexlog2html 

setup(name='latexlog2html',
      version = latexlog2html.__version__,
      author = latexlog2html.__author__ , 
      author_email = latexlog2html.__email__,
      url = 'http://github.com/johnjosephhorton/latexlog2html',
      packages = [''],
      package_data = {'':[]},
      package_dir= {'':'.'}, 
      entry_points={
          'console_scripts':
              ['latexlog2html = latexlog2html:main',
               ]}, 
      classifiers=(
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License v3 or '
          'later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      )
      )
