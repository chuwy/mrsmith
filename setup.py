#!/usr/bin/env python

from setuptools import setup

from mrsmith import __version__

setup(name='mrsmith',
      version=__version__,
      description=open('README.rst', 'r').read(),
      author='Anton Parkhomenko',
      author_email='mailbox@chuwy.me',
      url='http://chuwy.ru/mrsmith',
      install_requires=['python-gnupg'],
      packages=['mrsmith'],
      scripts=['bin/mrsmith'],
      license='MIT'
      )
