import socket
# prepare
sock = socket.socket()
sock.connect(('localhost', 8080))

# connection <-> data
while True:
    msg = input()
    if msg == 'quit()':
        break
    sock.send(msg.encode('UTF-8')) # ->

data = sock.recv(1024) # <-
sock.close()

print(data)