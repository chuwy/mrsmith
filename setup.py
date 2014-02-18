#!/usr/bin/env python

from setuptools import setup


setup(name='mrsmith',
      version='0.0.1',
      description=open('README.rst', 'r').read(),
      author='Anton Parkhomenko',
      author_email='anton@chuwy.ru',
      url='http://chuwy.ru/mrsmith',
      install_requires=['python-gnupg'],
      packages=['mrsmith'],
      scripts = ['bin/mrsmith'],
      license='MIT'
      )
