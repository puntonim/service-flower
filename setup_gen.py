#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pkgversion import list_requirements, pep440_version, write_setup_py
from setuptools import find_packages

write_setup_py(
    name='service-flower',
    version=pep440_version('1.0.1'),
    description="Flower service client",
    long_description=open('README.md').read(),
    author='puntonim',
    author_email='foo@gmail.com',
    url='https://github.com/puntonim/service-flower',
    install_requires=list_requirements('requirements/requirements-base.txt'),
    packages=find_packages(exclude=['tests']),
    tests_require=['tox'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
