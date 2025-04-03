import socket
skt = socket.socket()
port = 31111
skt.connect(('127.0.0.1', port))
print(skt.recv(1024)) # The parameter is the buffer
skt.close()
