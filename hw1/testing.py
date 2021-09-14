import sys
from client import Client

if __name__ == '__main__':
	a = Client(sys.argv[1])
	a.loop()