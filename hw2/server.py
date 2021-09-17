import socket

sock = socket.socket()
sock.bind(('localhost', 8080))
sock.listen(1)

conn, addr = sock.accept()
print('connected:', addr)
a = []
while True:
    data = conn.recv(1024)
    print(data.decode('UTF-8'))
    a.append(data)
    conn.send(a[0].upper())
    if not data:
        break


conn.close()
