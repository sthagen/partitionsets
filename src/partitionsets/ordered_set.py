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

from collections import Sequence


class OrderedSet(Sequence):
    """ Creates an ordered set from a list of tuples or
    other hashable items.  cf. [OrdSetImplPy] """

    def __init__(self, hashable_items):
        """ Save unique items of L in input order.  """
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

    def __setitem__(self, index):
        pass

    def __len__(self):
        return len(self.__oset)


def test():
    """ The call interface implemented as test function since
    it has a default behaviour if no input is given.  """
    import sys
    if len(sys.argv) > 1:
        ordered_set = OrderedSet(list(" ".join(sys.argv[1:]).split(" ")))
    else:
        print('Usage: %s member1 [m2 [m3 ... m25 ...]]' % (sys.argv[0],))
        print('Note: Order will be preserved but multiple identical'
              ' members replaced'
              ' by first occurence, i.e. A B C B maps to A B C')
        print(' ' * 4 + 'Sample run with default test case below:')
        ordered_set = OrderedSet(list('red green yellow blue'.split(" ")))
    print('{%s}' % (', '.join(ordered_set),))


if __name__ == '__main__':
    test()
