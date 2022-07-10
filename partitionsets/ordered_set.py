#! /usr/bin/env python
""" Minimal implementation of an ordered set for hashables
and feedback from [PyLint, Flake8].

References:

[Flake8]: https://pypi.python.org/pypi/flake8

[OrdSetImplPy]: http://code.activestate.com/recipes/576694/ (mixed with
    the simplified code from Don Sawatzky's comment, which is sufficient
    for this task)

[PyLint]: https://pypi.python.org/pypi/pylint

All python third party sources used are licensed under the MIT License.  """

import sys

if sys.version_info[0:2] > (3, 2):
    from collections.abc import Sequence
else:
    from collections import Sequence


class OrderedSet(Sequence):
    """Creates an ordered set from a list of tuples or
    other hashable items.  cf. [OrdSetImplPy]"""

    def __init__(self, hashable_items):
        """Save unique items of L in input order."""
        self.__map = {}
        self.__oset = []
        for item in hashable_items:
            if item not in self.__map:
                self.__map[item] = 1
                self.__oset.append(item)

    def __getitem__(self, index):
        return self.__oset[index]

    def __delitem__(self, index):
        pass

    def __setitem__(self, index, value):
        pass

    def __len__(self):
        return len(self.__oset)
