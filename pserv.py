#!/usr/bin/python

import SocketServer

class Handlr(SocketServer.BaseRequestHandler):
	""" Intro """
	def handle(self):
	        self.data = self.request.recv(1024).strip()
        	print "{} wrote:".format(self.client_address[0])
	        print self.data

	        self.request.sendall(self.data.upper())

if __name__ == "__main__":
	HOST, PORT = "localhost", 9999

	server = SocketServer.TCPServer((HOST, PORT), Handlr)

	server.serve_forever()

