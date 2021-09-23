import socket
from threading import Thread

def recieve(connection):
	answer = []
	while True:  # collect the full packet
		part_of_data = connection.recv(SIZE_OF_PART)
		answer.append(part_of_data)
		if len(part_of_data) < SIZE_OF_PART:
			break
	return ''.join(part.decode('UTF-8') for part in answer)

def recieve_file(connection):
	with open('new_file.txt', 'wb') as f:
		while True:
			data = connection.recv(SIZE_OF_PART)
			while data:
				f.write(data)
				data = connection.recv(SIZE_OF_PART)
				if len(data) < SIZE_OF_PART:
					f.write(data)
					break
			break

class ClientThread(Thread):
	def __init__(self, client_adress, clientsocket):
		Thread.__init__(self)
		self.conn = clientsocket
		self.addr = client_adress
		print('connected', self.addr)

	def run(self):
		with self.conn:
			while True:
				result = recieve(self.conn)
				if 'file' in result:
					recieve_file(self.conn)
				elif 'text' in result:
					text = recieve(self.conn)
					print(text, f'from {addr}')
				self.conn.send(b'OK')
				if 'quit()' in result:
					print(self.addr, 'Has disconnected')
					break


SIZE_OF_PART = 10
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8083))

threads = []
while len(threads) < 2:
	sock.listen(1)
	conn, addr = sock.accept()
	new_thread = ClientThread(addr, conn)
	threads.append(new_thread)
	new_thread.start()

for thread in threads:
	thread.join()

print('exit')
sock.close()