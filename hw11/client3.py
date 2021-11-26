import socket
from threading import Thread
import pickle
from time import sleep

SIZE_OF_PART = 1024

class Client3:
	def __init__(self, ip, port):
		self.connect(ip, port)

	def recieve(self):
		return pickle.loads(self.sock.recv(SIZE_OF_PART))

	def send(self):
		# data = pickle.dumps(Example('data_example', 1, 2))
		data = ('string', [1,2,3], {1: 2, 2: 3, 4: 5}, {1, 2, 3}, ('s', 't', 'r'))
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
