import os
import threading
from time import sleep
from MySocket import MySocket

class Server(threading.Thread):
	def __init__(self, index):
		threading.Thread.__init__(self)
		self.http_protocol = {
			'content-type': None,
			'content': None
		}
		self.connection = MySocket(f'socket{index}')
	# initialization if socket file is not exist

	def run(self):
		while True:
			# get the data from the client
			data = self.connection.read()
			# check if it is an our 'http' protocol
			# ToDo make it as an object of Protocol class!
			if isinstance(data, dict):
				print(f"data ({type(data)}): {data}")
				if data.get('content-type') == 'command':
					exec(data.get('content'))
				elif data.get('content-type') == 'file':
					path_file = data.get('content')
					if os.path.exists(path_file):
						os.popen(f'copy {path_file} {os.getcwd()}')
				elif data.get('content-type') == 'text':
					print(data.get('content'))
				# clean the socket
				self.connection.write(None)
			# ToDo in future our server will sleep unit the new data incoming. Now it is just simplification
			sleep(1)

if __name__ == '__main__':
	for i in range(1, 11):
		serv = Server(i)
		serv.start()
