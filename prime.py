#!/usr/bin/python2

import sys

max = sys.argv[1]
print x
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			break
	else:
		# loop fell through without finding a factor
		print n, 'is a prime number'
