#! /usr/bin/env python

from __future__ import print_function
from setuptools import setup
from distutils.core import setup as setupexe

import io
import os
import sys
import py2exe
import dummy2

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.txt','requirements.txt','changes.txt',)

setup(
    name='dummy2',
    version=dummy2.__version__,
    url='http://github.com/hn269/dummy2/',
    license='Cornell University',
    author='Hoang Long Nguyen',
    author_email='hn269@cornell.com',
    description='Dummy package adding, subtracting or multiplying two numbers - to try releasing a Python package',
    long_description=long_description,
    packages=['dummy2',],
    data_files=[('',['requirements.txt','changes.txt','icons\Dummy_icon.ico']),],)
    
setupexe(
    name='dummy2',
    packages=['dummy2',],
    windows=[
        {
        "script":'dummy2\dummy2a.py',
        "icon_resources": [(0,"Dummy_icon.ico")],
        }],
    console=[{
        "script":'dummy2\dummy2a.py',
        "icon_resources": [(0,"Dummy_icon.ico")],
        }],
    #zip_safe = True,
)