# Usage

To use PartitionSets in a project:

```python
import partitionsets
```

Typical usage in python code might look like this:

```python
#! /usr/bin/env python

from __future__ import print_function
from partitionsets import ordered_set
from partitionsets import partition

a_list = 'red green yellow blue'.split(" ")
an_oset = ordered_set.OrderedSet(a_list)
a_partition = partition.Partition(ordered_set)
for a_part in a_partition:
    print(a_part)
```

The sript `partition-sets` inside the bin folder may offer useful commands.
For usage info run it with the `-h` help option:

```console
❯ partition-sets -h
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
```
## Notes

Note this implementation works only for sets with 25 members or less.

This constraint is considered quite reasonable, as the method (constructing an
integer index) for larger numbers starts to overflow. Remember: The number of
partitions very steeply rises with each additional member considerably ...
