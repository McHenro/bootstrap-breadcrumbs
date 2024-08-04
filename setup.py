#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :copyright: Copyright 2013 by Łukasz Mierzwa
    :contact: l.mierzwa@gmail.com
"""

from __future__ import unicode_literals
from setuptools import setup, find_packages

setup(
    name='django_bootstrap_breadcrumbs',
    version='0.9.2',
    url='http://prymitive.github.com/bootstrap-breadcrumbs',
    license='MIT',
    description='Django breadcrumbs for Bootstrap 2, 3 or 4',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Łukasz Mierzwa',
    author_email='l.mierzwa@gmail.com',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'six',
        'Django>=4.0',  # Add Django as a dependency
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Framework :: Django',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    zip_safe=False,
    include_package_data=True,
)
