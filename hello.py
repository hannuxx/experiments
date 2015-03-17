#!/usr/bin/python2

f=open("foo")
line = f.readline()
while line:
	print line,	# omit NL
	# print(line,end='')
	line=f.readline()

f.close

