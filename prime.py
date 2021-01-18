#!/usr/bin/python3

import sys

s1=""
s2=""
x=0
if len(sys.argv) >= 3:
	s1 = sys.argv[1]
	s2 = sys.argv[2]
else:
	print('Usage: prime.py <lower-bound> <upper-bound>')
	quit()
print(f"Range {s1}-{s2}")
i1=int(s1)
i2=int(s2)
print("Primes:")
for n in range(i1, i2):
	for x in range(2, n):
		if n % x == 0:
			break
	else:
		print(n) # loop fell through without finding a factor
