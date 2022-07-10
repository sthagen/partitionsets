#! /usr/bin/env python
""" Minimal implementation of a partitioning class for sets based
on [PartImplPy] and feedback from [PyLint, Flake8].

All python sources are licensed under the MIT License.
As entry point for further research cf. [PartOfASet_WP]

References:

[Flake8]: https://pypi.python.org/pypi/flake8

[PartImplPy]: http://code.activestate.com/recipes/577211/ (r1)

[PartOfASet_WP]: Wikipedia entry Partition_of_a_set at
    http://en.wikipedia.org/wiki/Partition_of_a_set

[PyLint]: https://pypi.python.org/pypi/pylint


"""
from __future__ import print_function

from collections import defaultdict


class Partition:
    """Sets of only a few items already have many ways they can be partitioned
    into subsets. Therefore it can be useful to generate these partitions by
    index, like the partition class were some large list where one can just
    access element "i". Of course one should not compute the whole list in
    advance but compute the partitions on the fly. This recipe was originally
    extracted form a book by Kreher and Stinson. Over the years I came back to
    my code from time to time creating a new and hopefully more pythonic
    version each time I understood it better. My current take on it is that the
    algorithm looks a lot like creating a Pascals triangle in order to compute
    combinations. One just tries to find a way down the triangle to a specific
    element, each time subtracting the amounts the different positions in the
    triangle account for. It is also similar to finding indexed permutations of
    a set with elements occurring more than once. One of these days I will
    perhaps understand how all of this fits together. Until then I'll post code
    solving specific situations. cf. [PartImplPy]"""

    def __init__(self, ordered_set):
        self.data = list(ordered_set)
        self.n_data = len(ordered_set)
        self.table = self.rgf_table()

    def __getitem__(self, i):
        """Generates set partitions by index"""
        if i > len(self) - 1:
            raise IndexError
        a_list = self.unrank_rgf(i)
        result = self.as_set_partition(a_list)
        return result

    def __len__(self):
        return self.table[self.n_data, 0]

    def __delitem__(self, index):
        pass

    def __setitem__(self, key, value):
        pass

    def as_set_partition(self, a_list):
        """Transform a restricted growth function into a partition"""
        n_list = max(a_list[1:] + [1])
        n_data = self.n_data
        data = self.data
        partition = [[] for _ in range(n_list)]
        for i in range(n_data):
            partition[a_list[i + 1] - 1].append(data[i])
        return partition

    def rgf_table(self):
        """Compute the table values, but: The key line in the algorithm is
        D[i,j] = j * D[i-1,j] + D[i-1,j+1] which identifies D[i,j] as the
        number of ways to add i new items to a partition that already has
        j blocks. So e.g. D[1, j] = j+1 because a new
        item can be added to a partition having j blocks by adding it to any
        existing block or by having it start its own new block. Thus D[i,0] is
        the number of ways to partition the set {1, ..., i}.

        To solve this problem for combinations (i.e. get the i-th subset of a
        set), just take the binary representation of the index i, right? The
        places where 1's occur tell you which items to keep -- no need to
        generate Pascal's triangle"""
        n_data = self.n_data
        a_dict = defaultdict(lambda: 1)
        for i in range(1, n_data + 1):
            for j in range(0, n_data - i + 1):
                a_dict[i, j] = j * a_dict[i - 1, j] + a_dict[i - 1, j + 1]
        return a_dict

    def unrank_rgf(self, r_saught):
        """Unrank a restricted growth function"""
        n_data = self.n_data
        a_list = [1 for _ in range(n_data + 1)]
        j = 1
        a_dict = self.table
        for i in range(2, n_data + 1):
            v_j = a_dict[n_data - i, j]
            cr_j = j * v_j
            if cr_j <= r_saught:
                a_list[i] = j + 1
                r_saught -= cr_j
                j += 1
            else:
                a_list[i] = r_saught // v_j + 1
                r_saught %= v_j
        return a_list
