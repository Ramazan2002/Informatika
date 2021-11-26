import socket
from threading import Thread
import pickle

BUFFER = 1024
class Example:
	def __init__(self):
		self.__name = None
		self.__x = None
		self.__y = None
	def name(self):
		return self.__name

	def x(self):
		return self.__x

	def y(self):
		return self.__y

class Client:
	def __init__(self):
		self.__address = None
		self.__connection = None
		self.__name = None

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, x):
		self.__name = x

	@property
	def address(self):
		return self.__address

	@address.setter
	def address(self, x):
		self.__address = x

	@property
	def connection(self):
		"""
		Returns:
			socket.socket: connection
		"""
		return self.__connection

	@connection.setter
	def connection(self, x):
		self.__connection = x

class Server:
	def __init__(self, ip, port):
		self.clients = set()
		self.sock = socket.socket()
		self.sock.bind((ip, port))

		self.listen()

	def listen(self):
		print('Start')
		self.sock.listen(2)
		while True:
			connection, address = self.sock.accept()

			client = Client()
			client.address = address
			client.connection = connection

			self.clients.add(client)

			print(f'Connected {address}')
			Thread(target=self.client_loop, args=(client, )).start()

	def recv_and_share(self, client, new_client=False):
		try:
			if response := client.connection.recv(BUFFER):
				response = pickle.loads(response)
				if new_client:
					client.name = response
					if isinstance(response, Example):
						print(f'new client {client.address} with name: {response.name}')
					else:
						print(f'new client {client.address} with name: {client.name}')

					self.send_all(client, 'Привет всем, я новенький!')
					if isinstance(response, Example):
						client.connection.send(pickle.dumps(f'Ваше сообщение отправлено'
															f'{response.name, response.x, response.y}'))
					else:
						client.connection.send(pickle.dumps(f'Ваше сообщение отправлено, {response}'))
				else:
					if isinstance(response, Example):
						print(f'from client {client.address} recieved: {response.name, response.x, response.y}')
						self.send_all(client, f'{response.name, response.x, response.y}')
						client.connection.send(pickle.dumps(f'Ваше сообщение отправлено {response.name, response.x, response.y}'))
					else:
						print(f'from client {client.address} recieved: {response}')
						self.send_all(client, response)
						client.connection.send(pickle.dumps(f'Ваше сообщение отправлено {response}'))
			else:
				raise Exception('Client disconnected')

		except Exception:
			self.close_client(client)
			return False
		else:
			return True

	def client_loop(self, client):
		"""

		Args:
			client (Client):

		Returns:

		"""
		self.recv_and_share(client, new_client=True)
		while self.recv_and_share(client):
			pass

	def send_all(self, from_client, text):
		for client in self.clients:
			if client != from_client:
				client.connection.send(pickle.dumps(f"[{from_client.name}]: {text}"))

	def close_client(self, client):
		self.clients.remove(client)
		client.connection.close()

server = Server('localhost', 8080)
