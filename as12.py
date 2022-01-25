import socket
mys = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mys.connect(('data.pr4e.org',80))

c = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mys.send(c)

while True:
    data = mys.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mys.close()
