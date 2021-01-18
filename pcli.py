#!/usr/bin/python3

import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 9999))

s.sendall(b'Hello, world')
back = str(s.recv(1024), 'utf-8')
print(back)

