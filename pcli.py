#!/usr/bin/python

import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 9999))

ss = "Hello from Python!"
s.send(struct.pack('s', ss))
print 'Sent: ', ss

chunk = s.recv(256)
print 'Received: ', chunk

