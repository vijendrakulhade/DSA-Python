# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='DSA-Python',
    version='0.1.0',
    description='DSA Problems and solution in Python',
    long_description=readme,
    author='Vijendra Kulhade',
    author_email='vkulhade@asu.edu',
    url='https://github.com/vijendrakulhade/DSA-Python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
