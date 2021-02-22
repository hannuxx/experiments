#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    x = []
    tot = []
    for c in range(4):
        for i in range(4):
            b = i + 3
            r1 = arr[i:b]
            d = c + 3
            e1 = c + 1
            e2 = e1 + 1
            c1 = r1[0][c:d]
            c2 = r1[1][e1:e2]
            c3 = r1[2][c:d]
            t = sum(c1) + sum(c2) + sum(c3)
            tot.append(t)
    ret = -1000000
    for t in tot:
        if (t > ret):
            ret = t
    return ret

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open("output.txt", 'w')
    fin = open("hourglass.txt", 'r')

    arr = []

    for _ in range(6):
        input = fin.readline()
        #arr.append(list(map(int, input().rstrip().split())))
        arr.append(list(map(int, input.rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')
    
    print(f'{result}')

    fptr.close()
    fin.close()
