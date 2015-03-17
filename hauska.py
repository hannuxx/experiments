#!/usr/bin/python 

def hauska(n): return lambda n: n**n

f = hauska(7)

print  f, f(14)

