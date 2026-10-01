#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverse_words_order_and_swap_cases' function below.

def reverse_words_order_and_swap_cases(sentence):
    coll = sentence.strip().split()
    coll.reverse()
    fixed = ""
    for s in coll:
        fixed += s.swapcase() + " "
    return fixed.strip()

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open("output.txt", 'w')
    fin = open("rev_and_swap.txt", 'r')

    sentence = fin.readline()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
