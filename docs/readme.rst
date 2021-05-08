.. include:: ../README.rst

==============
Partition Sets
==============

Partition Sets provides a consolidated set of recipes gently provided by other
users over the years and under the MIT license. I modified these slightly so
that they now equally work under python2 and python3. All bugs are mine ;-)

You may find it useful for tasks involving small sets and also multi sets/bags.

Install
=======

A simple ``pip install PartitionSets`` should suffice.


Usage
=====

Typical usage in python code might look like this::

	#!/usr/bin/env python

	from __future__ import print_function
	from partitionsets import ordered_set
	from partitionsets import partition

	a_list = 'red green yellow blue'.split(" ")
	an_oset = ordered_set.OrderedSet(a_list)
	a_partition = partition.Partition(ordered_set)
	for a_part in a_partition:
		print (a_part)


The sript ``partition-sets`` inside the bin folder may offer useful commands.
For usage info run it with the ``-h`` help option::

	$> partition-sets -h
	usage: partition-sets [-h] [-q | -v] [-o OUT_FILENAME] [-T {text,csv,json}]
							 [-b] [-m]
							 element [element ...]

	partitioning of small sets with 25 or less members

	positional arguments:
	  element               define set as list of elements separated by spaces

	optional arguments:
	  -h, --help            show this help message and exit
	  -q, --quiet
	  -v, --verbosity       increase output verbosity
	  -o OUT_FILENAME, --out-filename OUT_FILENAME
							out file name if specified, else all sent to stdout
	  -T {text,csv,json}, --type {text,csv,json}
							type of output (format), defaults to text
	  -b, --bell-numbers    export the Bell numbers known by package
	  -m, --multi-set       handle elements as being par tof a multiset or bag



Notes
=====

Note this implementation works only for sets with 25 members or less.

This constraint is considered quite reasonable, as the method (constructing an
integer index) for larger numbers starts to overflow. Remember: The number of
partitions very steeply rises with each additional member considerably ...


Thanks also to
==============

This package merely wraps up several recipes (and comments) gently provided
under the MIT license through several people. Those I noticed have been noted below.
Any missing names are my fault. In case I get notified, I will try
to update, add or remove items in below lists accordingly.

Partition
---------

* Anton Vredegoor

* Chris Haulk

OrderedSet
----------

* Don Sawatzky

* Emil Wall

* Raymond Hettinger

Misc
----

* Nathan Hurst send feedback and a patch for version 0.1.1 - thanks


For further reference please see the comments of the module files.

References
==========

[A0001101]: "Bell or exponential numbers: ways of placing n labeled balls
	into n indistinguishable boxes." at http://oeis.org/A000110

[BellNumber]: Wikipedia entry Bell_number
	at https://en.wikipedia.org/wiki/Bell_number

[OEIS]: Wikipedia entry On-Line_Encyclopedia_of_Integer_Sequences at
	https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences

[Flake8]: https://pypi.org/project/flake8/

[OrdSetImplPy]: http://code.activestate.com/recipes/576694/ (mixed with
	the simplified code from Don Sawatzky's comment, which is sufficient
	for this task)

[PartImplPy]: http://code.activestate.com/recipes/577211/ (r1)

[PartOfASet_WP]: Wikipedia entry Partition_of_a_set at
	https://en.wikipedia.org/wiki/Partition_of_a_set

[PyLint]: https://pypi.org/project/pylint/
