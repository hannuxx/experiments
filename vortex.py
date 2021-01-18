#!/usr/bin/python3

import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("vortex.labs.overthewire.org", 5842))

ix = []
sum = 0
for i in range(4):
	chunk = s.recv(4)
	unp = struct.unpack('I', chunk)
	ix.append(unp[0])
	sum = sum + unp[0]
	print('chunk: ', chunk, ' -- struct.unpack: ', unp)

print('Sum: ', sum, ' -- ix: ', ix)

s.send(struct.pack('I', sum))

chunk = s.recv(256)
print(chunk)

