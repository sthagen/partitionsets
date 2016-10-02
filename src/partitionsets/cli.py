"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later,
  but that will cause problems: the code will get executed twice:

  - When you run `python -mpartitionsets` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``partitionsets.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``partitionsets.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
from __future__ import print_function

import argparse
import json
import sys

from partitionsets import partition, ordered_set, data_proxy


def main(argv=None):
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Partitioning of small sets with 25 or less members as given
    per command line arguments. A set may **not** contain
    multiple instances of a single element.

    References:

    [A0001101]: "Bell or exponential numbers: ways of placing n labeled balls
        into n indistinguishable boxes." at http://oeis.org/A000110

    [BellNumber]: Wikipedia entry Bell_number
        at http://en.wikipedia.org/wiki/Bell_number

    [OEIS]: Wikipedia entry On-Line_Encyclopedia_of_Integer_Sequences at
        http://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences

    [PartOfASet_WP]: Wikipedia entry Partition_of_a_set at
        http://en.wikipedia.org/wiki/Partition_of_a_set
    """
    argv = sys.argv if argv is None else argv

    BELLS = data_proxy.bell_number_data()
    N_BELLS_OK = 25  # could be len(bells), but overflows forbid that :-)
    parser = argparse.ArgumentParser(
        description="partitioning of small sets with 25 or less members")
    group = parser.add_mutually_exclusive_group()
    # group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    group.add_argument(
        "-v", "--verbosity", action="count", default=0,
        help="increase output verbosity")
    parser.add_argument(
        '-o', '--out-filename', action='store', nargs=1,
        help='out file name if specified, else all sent to stdout',
        required=False)
    parser.add_argument(
        "-T", "--type", type=str, choices=['text', 'csv', 'json'],
        default="text",
        help="type of output (format), defaults to text")
    parser.add_argument("-b", "--bell-numbers", action="store_true",
                        help="export the Bell numbers known by package")
    parser.add_argument(
        "-m", "--multi-set", action="store_true",
        help="handle elements as being par tof a multiset or bag")

    parser.add_argument(
        "element", nargs="+",
        help="define set as list of elements separated by spaces")
    args = parser.parse_args(argv)

    out_file = False
    if args.out_filename:
        out_file = ''.join(args.out_filename)
        print('Requested file ' + out_file + ' for output is ignored'
              ' in this version, sorry.')
    if args.bell_numbers:
        if not args.type or args.type == 'text':
            for n in range(0, len(BELLS)):
                print("%2d: %20d" % (n, BELLS[n]))
        elif args.type == 'json':
            p_map = {'d': {}}
            p_map['d']['bellNumbers'] = []
            for n in range(0, len(BELLS)):
                p_map['d']['bellNumbers'].append(BELLS[n])
            print(json.dumps(p_map))
        else:
            # must be args.type == 'csv' since choices are checked beforehand
            for n in range(0, len(BELLS)):
                print("%d,%d" % (n, BELLS[n]))
        sys.exit(0)
    if args.element:
        if args.multi_set:
            AN_XSET = list(" ".join(args.element).split(" "))
        else:
            AN_XSET = ordered_set.OrderedSet(
                list(" ".join(args.element).split(" ")))
    if args.verbosity >= 2:
        print('Even a small class, such as {%s},' % (', '.join(AN_XSET),),
              end=" ")
        print('can be partitioned in a surprising number of different ways:')
    N_X_S = len(AN_XSET)
    BELL_NUMBER = BELLS[N_X_S - 1] if N_X_S < N_BELLS_OK else BELLS[N_BELLS_OK]
    if N_X_S > N_BELLS_OK:
        print('Error: Not prepared for %d partitions.' % (N_X_S,))
        print('       Sorry. Please use %d members or less.' % (N_BELLS_OK,))
        sys.exit(1)
    A_PARTITION = partition.Partition(AN_XSET)
    if not args.type or args.type == 'text':

        for a_part in A_PARTITION:
            d_part = repr(a_part)
            if args.verbosity >= 1:
                d_part = d_part.replace('[', '{').replace(']', '}')
            if args.verbosity >= 2:
                d_part = d_part.replace("'", '')
            if args.verbosity:
                print('    ' + '* ' + d_part)
            else:
                print(d_part)

        if args.verbosity:
            print('    ' + '=> (Number of partitions = %d,'
                  % (len(A_PARTITION),), end=" ")
            print('expected is %d)' % (BELL_NUMBER,))
        if args.verbosity >= 3:
            print('Procedure class-partitions takes one argument, a', end=" ")
            print('finite class C(members separated by one or more', end=" ")
            print('spaces) and returns an itemized list like above', end=" ")
            print('containing all partitions of C.  (Thus the result', end=" ")
            print('is a class of classes of classes of members', end=" ")
            print('of C.)')

    elif args.type == 'json':
        p_map = {'d': {}}
        if args.verbosity:
            p_map['d']['__metadata'] = {'set': list(AN_XSET),
                                        'bellNumber': BELL_NUMBER,
                                        'numberOfPartitions': len(A_PARTITION)
                                        }
        p_map['d']['partitions'] = []
        for a_part in A_PARTITION:
            p_map['d']['partitions'].append(a_part)
        print(json.dumps(p_map))
    else:  # must be args.type == 'csv' since choices are checked beforehand
        for a_part in A_PARTITION:
            N_P_S = len(a_part)
            r_map = []
            for s in a_part:
                r_map.append(' '.join(s))
            for i in range(N_P_S, N_X_S):
                r_map.append('')
            print(','.join(r_map))

    return 0
