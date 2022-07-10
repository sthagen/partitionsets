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

from partitionsets import ordered_set, partition


def parse_args(argv=None):
    """DRY and KISS."""

    parser = argparse.ArgumentParser(description='partitioning of small sets with 25 or less members')
    group = parser.add_mutually_exclusive_group()
    # group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')
    group.add_argument('-v', '--verbosity', action='count', default=0, help='increase output verbosity')
    parser.add_argument(
        '-o',
        '--out-filename',
        action='store',
        nargs=1,
        help='out file name if specified, else all sent to stdout',
        required=False,
    )
    parser.add_argument(
        '-T',
        '--type',
        type=str,
        choices=['text', 'csv', 'json'],
        default='text',
        help='type of output (format), defaults to text',
    )
    parser.add_argument('-b', '--bell-numbers', action='store_true', help='export the Bell numbers known by package')
    parser.add_argument(
        '-m', '--multi-set', action='store_true', help='handle elements as being part of a multiset or bag'
    )

    parser.add_argument('element', nargs='+', help='define set as list of elements separated by spaces')

    return parser.parse_args(argv)


def show_bell_numbers(args, bells):
    """Loosely coupled functionality."""

    if not args.type or args.type == 'text':
        for ndx in range(0, len(bells)):
            print('%2d: %20d' % (ndx, bells[ndx]))
    elif args.type == 'json':
        p_map = {'d': {}}
        p_map['d']['bellNumbers'] = []
        for ndx in range(0, len(bells)):
            p_map['d']['bellNumbers'].append(bells[ndx])
        print(json.dumps(p_map))
    else:
        # must be args.type == 'csv' since choices are checked beforehand
        for ndx in range(0, len(bells)):
            print('%d,%d' % (ndx, bells[ndx]))
    sys.exit(0)


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

    bells = [
        1,
        2,
        5,
        15,
        52,
        203,
        877,
        4140,
        21147,
        115975,
        678570,
        4213597,
        27644437,
        190899322,
        1382958545,
        10480142147,
        82864869804,
        682076806159,
        5832742205057,
        51724158235372,
        474869816156751,
        4506715738447323,
        44152005855084346,
        445958869294805289,
        4638590332229999353,
        49631246523618756274,
    ]

    n_bells_ok = 25  # could be len(bells), but overflows forbid that :-)
    args = parse_args(argv)

    out_file = False
    if args.out_filename:
        out_file = ''.join(args.out_filename)
        print('Requested file ' + out_file + ' for output is ignored' ' in this version, sorry.')
    if args.bell_numbers:
        show_bell_numbers(args, bells)  # will not return
    if args.element:
        if args.multi_set:
            an_xset = list(' '.join(args.element).split(' '))
        else:
            an_xset = ordered_set.OrderedSet(list(' '.join(args.element).split(' ')))
    if args.verbosity >= 2:
        print(
            'Even a small class, such as {%s},'
            ' can be partitioned in a surprising'
            ' number of different ways:' % (', '.join(an_xset),)
        )
    n_x_s = len(an_xset)
    bell_number = bells[n_x_s - 1] if n_x_s < n_bells_ok else bells[n_bells_ok]
    if n_x_s > n_bells_ok:
        print(
            'Error: Not prepared for %d partitions.'
            '       Sorry. Please use %d members or less.'
            ''
            % (
                n_x_s,
                n_bells_ok,
            )
        )
        sys.exit(1)
    a_partition = partition.Partition(an_xset)
    if not args.type or args.type == 'text':

        for a_part in a_partition:
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
            print(
                '    ' + '=> (Number of partitions = %d,'
                ' expected is %d)'
                % (
                    len(a_partition),
                    bell_number,
                )
            )
        if args.verbosity >= 3:
            print(
                'Procedure class-partitions takes one argument, a'
                ' finite class C(members separated by one or more'
                ' spaces) and returns an itemized list like above'
                ' containing all partitions of C.  (Thus the result'
                ' is a class of classes of classes of members'
                ' of C.)'
            )

    elif args.type == 'json':
        p_map = {'d': {}}
        if args.verbosity:
            p_map['d']['__metadata'] = {
                'set': list(an_xset),
                'bellNumber': bell_number,
                'numberOfPartitions': len(a_partition),
            }
        p_map['d']['partitions'] = []
        for a_part in a_partition:
            p_map['d']['partitions'].append(a_part)
        print(json.dumps(p_map))
    else:  # must be args.type == 'csv' since choices are checked beforehand
        for a_part in a_partition:
            n_p_s = len(a_part)
            r_map = []
            for a_p in a_part:
                r_map.append(' '.join(a_p))
            r_map += ['' for __ in range(n_p_s, n_x_s)]
            print(','.join(r_map))

    return 0
