import os
import pickle

class MySocket:
	def __init__(self, name):
		# if socket is not created before
		if not os.path.exists(name):
			with open(name, 'wb') as file:
				pickle.dump(None, file)
		self.stream = open(name, 'rb+')

	def write(self, protocol):
		# move the pointer to the beginning
		self.stream.seek(0)
		# write the bytes as pickle
		pickle.dump(protocol, self.stream)
		# truncate the file's size based on written data
		self.stream.truncate()

	def read(self):
		# move the pointer to the beginning
		self.stream.seek(0)
		return pickle.load(self.stream)
