#!/usr/bin/python

"""
usage:   shuffle.py  -f <file_name>, --file <file_name> -b <number of bytes>, --bytes <number of bytes>
						[--dry-run]
						[-h, --help]
"""
from __future__ import print_function
import sys
import os
import argparse
import inspect
import random

def get_top_dir():
    """
    Returns the absolute path of the project's top directory, i.e. the root folder
    of the repository's directory tree (at present, this file MUST be located there).
    """
    return os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda:0)))

def get_option_list():
    """
    Returns the list of available options.
    """
    return ["AES-256", "Special", "Plain"]

def run(args):
    """
    Shuffle random bytes on the file

    """

    verbose = False
    fn = ""
    bytes = 1024
    if args.verbose:
        verbose = True
    if args.file:
        fn = args.file
    if args.bytes:
        bytes = int(args.bytes);

    c = []
    for x in range(1, bytes):
        c.append(random.randrange(0, 256))

    for a in c:
        print("%x" % a, end='')

    print("\n")
    tx = []
    for b in range(0, 256):
        x = (c.count(b), b)
        tx.append(x)

    tx.sort()

    r = 0
    for i in range(0, 256, 10):
        mx = 10
        if (i >= 250):
            mx = 256 - i
        for j in range(0, mx):
            t1 = (i+j,)
            t2 = t1 + tx[i+j]
            print("%d: %d\t%x\t" % t2, end='')
            r += 1

# THE START OF MAIN
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Do random shuffle of N bytes to the file.')
    parser.add_argument("-f", "--file", help="File to be written",)
    parser.add_argument("-b", "--bytes",
        nargs='?', const='1024', default='1024',
        help="The amount of bytes to be written",)
    parser.add_argument("--dry-run",
        help="Show action without actually writing to the file",
        action="store_true")
    parser.add_argument("-v", "--verbose",
        help="Increase displayed information",
        action="store_true")   
    args = parser.parse_args()

    if args.dry_run:
        print("\nshuffle {0}<\n".format(vars(args)))
    else:
        run(args)
# THE END OF MAIN
