========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-case-changer/badge/?style=flat
    :target: https://readthedocs.org/projects/python-case-changer
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/philipptempel/python-case-changer.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/philipptempel/python-case-changer

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/philipptempel/python-case-changer?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/philipptempel/python-case-changer

.. |requires| image:: https://requires.io/github/philipptempel/python-case-changer/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/philipptempel/python-case-changer/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/philipptempel/python-case-changer/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/philipptempel/python-case-changer

.. |version| image:: https://img.shields.io/pypi/v/case-changer.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/case-changer

.. |wheel| image:: https://img.shields.io/pypi/wheel/case-changer.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/case-changer

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/case-changer.svg
    :alt: Supported versions
    :target: https://pypi.org/project/case-changer

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/case-changer.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/case-changer

.. |commits-since| image:: https://img.shields.io/github/commits-since/philipptempel/python-case-changer/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/philipptempel/python-case-changer/compare/v0.1.0...master



.. end-badges

A python port of the npm package `change-case <https://github.com/blakeembrey/change-case/>`_.

    Transform a string between camelCase, PascalCase, Capital Case, snake_case, param-case, CONSTANT_CASE and others.

* Free software: MIT license

Installation
============

::

    pip install case-changer

You can also install the in-development version with::

    pip install https://github.com/philipptempel/python-case-changer/archive/master.zip


Documentation
=============


https://python-case-changer.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
