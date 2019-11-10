========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires| |coveralls|
        | |scrutinizer| |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-partitionsets/badge/?style=flat
    :target: https://readthedocs.org/projects/python-partitionsets
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/sthagen/python-partitionsets.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/sthagen/python-partitionsets

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/sthagen/python-partitionsets?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/sthagen/python-partitionsets

.. |requires| image:: https://requires.io/github/sthagen/python-partitionsets/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/sthagen/python-partitionsets/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/sthagen/python-partitionsets/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/github/sthagen/python-partitionsets

.. |codeclimate| image:: https://codeclimate.com/github/sthagen/python-partitionsets/badges/gpa.svg
   :target: https://codeclimate.com/github/sthagen/python-partitionsets
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/partitionsets.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/PartitionSets/

.. |downloads| image:: https://img.shields.io/pypi/dm/partitionsets.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.org/project/PartitionSets/

.. |wheel| image:: https://img.shields.io/pypi/wheel/partitionsets.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.org/project/PartitionSets/

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/partitionsets.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.org/project/PartitionSets/

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/partitionsets.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.org/project/PartitionSets/

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/sthagen/python-partitionsets/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/sthagen/python-partitionsets/


.. end-badges

Consolidation of existing third party recipes for partitioning of sets and multisets/bags.

* Free software: MIT license

Installation
============

::

    pip install partitionsets

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
