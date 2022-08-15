# Partition Sets

Consolidation of existing third party recipes for partitioning of sets and multisets/bags.

Partition Sets provides a consolidated set of recipes gently provided by other
users over the years and under the MIT license. I modified these slightly so
that they now equally work under python2 and python3. All bugs are mine ;-)

You may find it useful for tasks involving small sets and also multi sets/bags.

[License: MIT](https://git.sr.ht/~sthagen/partitionsets/tree/default/item/LICENSE)

[![version](https://img.shields.io/pypi/v/partitionsets.svg?style=flat)](https://pypi.python.org/pypi/partitionsets/)
[![downloads](https://pepy.tech/badge/partitionsets/month)](https://pepy.tech/project/partitionsets)
[![wheel](https://img.shields.io/pypi/wheel/partitionsets.svg?style=flat)](https://pypi.python.org/pypi/partitionsets/)
[![supported-versions](https://img.shields.io/pypi/pyversions/partitionsets.svg?style=flat)](https://pypi.python.org/pypi/partitionsets/)
[![supported-implementations](https://img.shields.io/pypi/implementation/partitionsets.svg?style=flat)](https://pypi.python.org/pypi/partitionsets/)

## Bug Tracker

Feature requests and bug reports are best entered in the [todos of partitionsets](https://todo.sr.ht/~sthagen/partitionsets).

## Primary Source repository

The primary source of `partitionsets` lives somewhere on a mountain in Central Switzerland.
But, we use decentralized version control (git), so any clone can become the source to everyone's benefit, no central only code.
Anyway, the preferred public clones of `partitionsets` are:

* [on codeberg](https://codeberg.org/sthagen/partitionsets) - a collaboration platform and git hosting for free and open source software, content and projects.
* [at sourcehut](https://git.sr.ht/~sthagen/partitionsets) - a collection of tools useful for software development.

## Thanks also to

This package merely wraps up several recipes (and comments) gently provided
under the MIT license through several people. Those I noticed have been noted below.
Any missing names are my fault. In case I get notified, I will try
to update, add or remove items in below lists accordingly.

### Partition

* Anton Vredegoor
* Chris Haulk

### OrderedSet

* Don Sawatzky
* Emil Wall
* Raymond Hettinger

### Misc

* Nathan Hurst send feedback and a patch for version 0.1.1 - thanks


For further reference please see the comments of the module files.

## References

[A0001101]: "Bell or exponential numbers: ways of placing n labeled balls
	into n indistinguishable boxes." at http://oeis.org/A000110

[BellNumber]: Wikipedia entry Bell_number
	at https://en.wikipedia.org/wiki/Bell_number

[OEIS]: Wikipedia entry On-Line_Encyclopedia_of_Integer_Sequences at
	https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences

[Flake8]: https://pypi.org/project/flake8/

[OrdSetImplPy]: https://code.activestate.com/recipes/576694/ (mixed with
	the simplified code from Don Sawatzky's comment, which is sufficient
	for this task)

[PartImplPy]: https://code.activestate.com/recipes/577211/ (r1)

[PartOfASet_WP]: Wikipedia entry Partition_of_a_set at
	https://en.wikipedia.org/wiki/Partition_of_a_set

[PyLint]: https://pypi.org/project/pylint/
