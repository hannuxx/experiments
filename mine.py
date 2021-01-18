#!/usr/bin/python3

import sys, getopt
import time
from hashlib import sha256

MAX_UPPER = 100000000

def sha256Str(txt):
    ret = sha256(txt.encode('ascii')).hexdigest()
    return ret

def mine(d, bn, s, t, ph):
    t0 = time.clock()
    prefix_str = '0' * int(d)
    for n in range(MAX_UPPER):
        txt = str(bn) + t + ph + str(n)
        nh = sha256Str(txt)
        if (nh.startswith(prefix_str)):
            print(f'mine: FOUND: {nh} with {n}')
            tx = time.clock() - t0
            return nh, n, tx
    tx = time.clock() - t0
    return '', 0, tx

def input_hash(fn):
    f=open(fn)
    line = f.readline()
    ret = sha256Str(line)
    f.close();
    return ret

def output_hash(fn, nh, n, s):
    f = open(fn, "w+")
    f.write(nh)
    f.write('\n')
    f.write(str(n))
    f.write('\n')
    f.write(str(s))
    f.close();
    return nh, n

def main(argv):
    print(argv)
    ifile = ''
    ofile = ''
    difficulty = 1
    block_number = 1
    start_nonce = 0
    trans = ''
    prev_hash = ''

    try:
        opts, args = getopt.getopt(argv, 'hd:b:i:o:s:p:' ,["help=", "difficulty=", "block=", "input=", "output=", "start=", "prev="])
    except getopt.GetoptError:
        print("getopt ERROR!")
        help()

    for opt, arg in opts:
        print('opt: ', opt, ' arg:', arg)
        if opt in ("-h", "--help"):
            help()
        elif opt in ("-d", "--difficulty"):
            difficulty = arg
        elif opt in ("-b", "--block"):
            block_number = arg
        elif opt in ("-i", "--input"):
            ifile = arg
        elif opt in ("-o", "--output"):
            ofile = arg
        elif opt in ("-s", "--start"):
            start_nonce = arg
        elif opt in ("-s", "--prev"):
            prev_hash = arg
    print(f'Params are: difficulty: {difficulty}, blblock_number: {block_number}, ifile: {ifile}, ofile: {ofile}, start_nonce: {start_nonce}, prev_hash: {prev_hash}')
    trans = input_hash(ifile)
    new_hash, nonce, secs = mine(difficulty, block_number, start_nonce, trans, prev_hash)
    if (len(new_hash) > 0):
        print(f'New hash: {new_hash} with nonce: {nonce}, secs: {secs}')
        output_hash(ofile, new_hash, nonce, secs)

if __name__ == "__main__":
    main(sys.argv[1:])
