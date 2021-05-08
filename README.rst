========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |coveralls|
        | |scrutinizer| |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-partitionsets/badge/?style=flat
    :target: https://readthedocs.org/projects/python-partitionsets
    :alt: Documentation Status

.. |coveralls| image:: https://coveralls.io/repos/sthagen/python-partitionsets/badge.svg?branch=default&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/github/sthagen/python-partitionsets

.. |codeclimate| image:: https://api.codeclimate.com/v1/badges/2b595acdb05e494024dc/maintainability.svg
   :target: https://codeclimate.com/github/sthagen/python-partitionsets/builds
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/partitionsets.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/partitionsets/

.. |downloads| image:: https://img.shields.io/pypi/dm/partitionsets.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.org/project/partitionsets/

.. |wheel| image:: https://img.shields.io/pypi/wheel/partitionsets.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.org/project/partitionsets/

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/partitionsets.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.org/project/partitionsets/

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/partitionsets.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.org/project/partitionsets/

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/sthagen/python-partitionsets/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/sthagen/python-partitionsets/


.. end-badges

Historic consolidation of existing third party recipes for partitioning of sets and multisets/bags.

* Free software: MIT license

Installation
============

::

    pipx install partitionsets

or::

    python -m pip install partitionsets

Documentation
=============

https://python-partitionsets.readthedocs.io/en/latest/


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

**Note**: The name of the default branch is `default`.
