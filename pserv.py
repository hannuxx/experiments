#!/usr/bin/python3

import socketserver

class MyHandler(socketserver.BaseRequestHandler):
	""" Intro """
	def handle(self):
		self.data = self.request.recv(1024).strip()
		uData = self.data.decode("utf-8") 
		print("{}: {}".format(self.client_address[0], uData))
		self.request.sendall(self.data.upper())

if __name__ == "__main__":
	HOST, PORT = "localhost", 9999

	server = socketserver.TCPServer((HOST, PORT), MyHandler)

	server.serve_forever()
