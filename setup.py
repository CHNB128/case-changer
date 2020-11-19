#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
import re
from glob import glob
from os.path import basename, dirname, join, splitext
from setuptools import find_packages, setup


def read(*names, **kwargs):
    with io.open(
            join(dirname(__file__), *names),
            encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
        name='case-changer',
        version='0.1.0',
        license='MIT',
        description='A python port of the npm package `change-case`',
        long_description='%s\n%s' % (
                re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub(
                        '', read('README.rst')),
                re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
        ),
        author='Philipp Tempel',
        author_email='python@philipptempel.me',
        url='https://github.com/philipptempel/python-case-changer',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
        include_package_data=True,
        zip_safe=False,
        classifiers=[
                # complete classifier list:
                # http://pypi.python.org/pypi?%3Aaction=list_classifiers
                'Development Status :: 5 - Production/Stable',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Operating System :: Unix',
                'Operating System :: POSIX',
                'Operating System :: Microsoft :: Windows',
                'Programming Language :: Python',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Programming Language :: Python :: Implementation :: CPython',
                'Programming Language :: Python :: Implementation :: PyPy',
                'Topic :: Utilities',
        ],
        project_urls={
                'Documentation': 'https://python-case-changer.readthedocs.io/',
                'Changelog':
                                 'https://python-case-changer.readthedocs.io/'
                                 'en/latest/changelog.html',
                'Issue Tracker':
                                 'https://github.com/philipptempel/'
                                 'python-case-changer/issues',
        },
        keywords=[
                'case changer',
                'case conversion',
                'string manipulation',
        ],
        python_requires='!=2.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
        install_requires=[
                'click',
        ],
        extras_require={
        },
        entry_points={
                'console_scripts': [
                        'case-changer = case_changer.cli:cli',
                ]
        },
)
