#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 sts=4 tw=78 et:
# -----------------------------------------------------------------------------
import os
from setuptools import setup

this_directory = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='markdown_cjk_space',
    description='Python markdown extension for markup Emoji',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eloise Severin',
    url='https://github.com/EloiseSeverin/markdown_markup_emoji/',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    version='0.1.0',
    py_modules = ['markup_emoji'],
    install_requires=['Markdown>=3.0.0'],
)
