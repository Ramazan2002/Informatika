import socket
from threading import Thread
import pickle
from random import randint
from time import sleep

SIZE_OF_PART = 1024

class Client:
	def __init__(self, ip, port):
		self.connect(ip, port)

	def recieve(self):
		return self.sock.recv(SIZE_OF_PART).decode('UTF-8')

	def send(self):
		data = input('text: ').encode('UTF-8')
		self.sock.send(data)

	def read_socket(self):
		while True:
			data = self.recieve()
			print(data)

	def loop(self):
		self.thread = Thread(target=self.read_socket)
		self.thread.start()

		while True:
			self.send()

	def connect(self, ip, port):
		self.sock = socket.socket()
		self.sock.connect((ip, port))

		self.loop()

	def disconnect(self):
		self.thread.join()
		self.sock.close()
		print('exit')

client = Client('localhost', 8081)
client.loop()
