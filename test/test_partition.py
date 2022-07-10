#! /usr/bin/env python
""" This is the main partition test runner.
It discovers the tests available and runs them.  """

import unittest

from partitionsets import ordered_set, partition


class TestPartition(unittest.TestCase):
    """Tests for the Partition class."""

    def setUp(self):
        """Useful with integer parameter."""
        self.seq = range(3)
        self.x_len = 5
        self.parts = [
            [[0, 1, 2]],
            [[0, 1], [2]],
            [[0, 2], [1]],
            [[0], [1, 2]],
            [[0], [1], [2]],
        ]
        self.oset = ordered_set.OrderedSet(self.seq)

    def test_part(self):
        """Make sure the partition is constructable."""
        a_part = partition.Partition(self.oset)
        self.assertEqual(isinstance(a_part, partition.Partition), True)

    def test_len(self):
        """Test the __len__ method."""
        len_part = len(partition.Partition(self.seq))
        self.assertEqual(len_part, self.x_len)

    def test_get(self):
        """Test the __getitem__ method."""
        a_part = partition.Partition(self.oset)
        for i, perm in enumerate(self.parts):
            print(perm)
            print(a_part[i])
            self.assertEqual(a_part[i], perm)

    def test_del(self):
        """Test the __delitem__ dummy method."""
        a_part = partition.Partition(self.oset)
        b_part = partition.Partition(self.oset)
        del a_part[0]
        self.assertEqual(a_part[0], b_part[0])

    def test_set(self):
        """Test the __setitem__ dummy method."""
        a_part = partition.Partition(self.oset)
        b_part = partition.Partition(self.oset)
        a_part[0] = 'foo bar baz'
        self.assertEqual(a_part[0], b_part[0])


suite = unittest.TestLoader().loadTestsFromTestCase(TestPartition)
unittest.TextTestRunner(verbosity=2).run(suite)
