# Partition Sets

Consolidation of existing third party recipes for partitioning of sets and multisets/bags.

Partition Sets provides a consolidated set of recipes gently provided by other
users over the years and under the MIT license. I modified these slightly so
that they now equally work under python2 and python3. All bugs are mine ;-)

You may find it useful for tasks involving small sets and also multi sets/bags.

[![license](badges/license-spdx-mit.svg)](https://git.sr.ht/~sthagen/partitionsets/tree/default/item/LICENSE)
[![Country of Origin](badges/country-of-origin-name-switzerland-neutral.svg)](https://git.sr.ht/~sthagen/partitionsets/tree/default/item/COUNTRY-OF-ORIGIN)
[![Export Classification Control Number (ECCN)](badges/export-control-classification-number_eccn-ear99-neutral.svg)](https://git.sr.ht/~sthagen/partitionsets/tree/default/item/EXPORT-CONTROL-CLASSIFICATION-NUMBER)
[![Configuration](badges/configuration-sbom.svg)](third-party/index.html)

[![Version](https://img.shields.io/pypi/v/partitionsets.svg?style=flat)](https://pypi.python.org/pypi/partitionsets/)
[![Downloads](badges/downloads-per-month.svg)](https://pepy.tech/project/partitionsets)
[![Supported Versions](https://img.shields.io/pypi/pyversions/partitionsets.svg?style=flat)](https://pypi.python.org/pypi/partitionsets/)
[![Maintenance Status](badges/commits-per-year.svg)](https://git.sr.ht/~sthagen/partitionsets/log)

## Bug Tracker

Any feature requests or bug reports shall go to the [todos of partitionsets](https://todo.sr.ht/~sthagen/partitionsets).

## Primary Source repository

The main source of `partitionsets` is on a mountain in central Switzerland.
We use distributed version control (git).
There is no central hub.
Every clone can become a new source for the benefit of all.
The preferred public clones of `partitionsets` are:

* [on codeberg](https://codeberg.org/sthagen/partitionsets) - a democratic community-driven, non-profit software development platform operated by Codeberg e.V.
* [at sourcehut](https://git.sr.ht/~sthagen/partitionsets) - a collection of tools useful for software development.

## Contributions

Please do not submit "pull requests" (I found no way to disable that "feature" on GitHub).
If you like to share small changes under the repositories license please kindly do so by sending a patchset.
You can either send such a patchset per email using [git send-email](https://git-send-email.io) or 
if you are a sourcehut user by selecting "Prepare a patchset" on the summary page of your fork at [sourcehut](https://git.sr.ht/).

## Support

Please kindly submit issues at <https://todo.sr.ht/~sthagen/partitionsets> or write plain text email to <~sthagen/partitionsets@lists.sr.ht> to submit patches and request support. Thanks.

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
