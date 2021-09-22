import socket

# prepare
SIZE_OF_PART = 10
sock = socket.socket()
sock.connect(('localhost', 8083))

def recieve(connection):
	answer = []
	while True:  # collect the full packet
		part_of_data = connection.recv(SIZE_OF_PART)
		answer.append(part_of_data)
		if len(part_of_data) < SIZE_OF_PART:
			break
	return ''.join(part.decode('UTF-8') for part in answer)

def recieve_file(filename):
	with open(f'{filename}', 'rb') as f:
		l = f.read(SIZE_OF_PART)
		while l:
			sock.send(l)
			l = f.read(SIZE_OF_PART)

with sock:
	while True:
		type_of = input('write a type: ')
		sock.send(type_of.encode('UTF-8'))
		if type_of == 'file':
			filename = input('write a filename: ')
			recieve_file(filename)
		elif type_of == 'text':
			text = input('write a text: ')
			sock.send(text.encode('UTF-8'))
		answer = recieve(sock)
		print("get from server: ", answer)
		if 'quit()' in type_of:
			break
