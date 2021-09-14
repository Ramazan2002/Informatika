from MySocket import MySocket

class Client:
	def __init__(self, connection):
		# just a template of the "protocol" which will be used for filling data
		self.http_protocol = {
			'content-type': None,
			'content': None
		}
		# init the socket stream
		self.connection = MySocket(connection)

	def loop(self):
		while True:
			content_type = input('type of content ')
			content = input('content ')
			print('-' * 10)

			request = self.http_protocol.copy()
			request['content-type'] = content_type
			request['content'] = content

			self.connection.write(request)


