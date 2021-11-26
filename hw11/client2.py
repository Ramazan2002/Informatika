import socket
from threading import Thread
import pickle
from random import randint
from time import sleep

SIZE_OF_PART = 1024

class Client2:
	def __init__(self, ip, port):
		self.connect(ip, port)

	def recieve(self):
		return pickle.loads(self.sock.recv(SIZE_OF_PART))

	def send(self):
		data = {randint(0, 255): randint(-255, 0) for i in range(10)}
		sleep(0.5)
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

client2 = Client2('localhost', 8080)
client2.loop()
