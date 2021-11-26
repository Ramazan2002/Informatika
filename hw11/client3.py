import socket
from threading import Thread
import pickle
from time import sleep
from random import randint

SIZE_OF_PART = 1024


class Example:
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y

	def __str__(self):
		return f'{self.name, self.x, self.y}'

class Client3:
	def __init__(self, ip, port):
		self.connect(ip, port)

	def recieve(self):
		return pickle.loads(self.sock.recv(SIZE_OF_PART))

	def send(self):
		data = Example('example_name', randint(0, 10), randint(0, 10))
		sleep(0.25)
		self.sock.send(pickle.dumps(data))

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

client3 = Client3('localhost', 8080)
client3.loop()
