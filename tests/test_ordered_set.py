#! /usr/bin/env python
""" This is the main test runner.
It discovers the tests available and runs them.  """

import unittest

from partitionsets import ordered_set


class TestOrderedSet(unittest.TestCase):
    """ Tests for the OrderedSet class.  """

    def setUp(self):
        """ Useful with integer parameter. """
        self.seq = range(5)

    def test_oset(self):
        """ Make sure the ordered set cast does not lose any elements. """
        an_oset = list(ordered_set.OrderedSet(self.seq))
        self.assertEqual(an_oset, list(self.seq))

    def test_len(self):
        """ Test the __len__ method. """
        len_oset = len(ordered_set.OrderedSet(self.seq))
        self.assertEqual(len_oset, len(self.seq))

    def test_get(self):
        """ Test the __getitem__ method. """
        an_oset = ordered_set.OrderedSet(self.seq)
        for i in self.seq:
            self.assertEqual(an_oset[i], i)


suite = unittest.TestLoader().loadTestsFromTestCase(TestOrderedSet)
unittest.TextTestRunner(verbosity=2).run(suite)
