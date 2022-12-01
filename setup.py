#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Rabah Abdul Khalek",
    author_email='rabah@giskard.ai',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Model to predict if a a customer default or not ",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='credit_scoring_model',
    name='credit_scoring_model',
    packages=find_packages(include=['credit_scoring_model', 'credit_scoring_model.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rabah-khalek/credit_scoring_model',
    version='0.1.0',
    zip_safe=False,
)
