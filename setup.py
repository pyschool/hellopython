#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    name='hipyschool',
    version='1.0.6',
    description='A pyschool story for learning regular expressions.',
    long_description=readme + '\n\n' + history,
    author='Sophilabs',
    author_email='hi@sophilabs.co',
    url='https://github.com/pyschool/hipyschool',
    packages=['hipyschool'],
    entry_points={
        'console_scripts': [
            'hipyschool=hipyschool:Story.begin'
        ]
    },
    include_package_data=True,
    install_requires=[
        'story>=1.1.5'
    ],
    license='MIT license',
    zip_safe=False,
    keywords='hipyschool',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=[]
)
