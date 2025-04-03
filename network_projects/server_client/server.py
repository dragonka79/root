import socket
skt = socket.socket()
print(f"Socket is created successfully")
port = 31111
skt.bind(('', port)) # The first parameter (IP) is empty, the server can receive requests from any IPs.
print(f'Socket binded to port {port}')
skt.listen(5) # The server can listen upto 5 different connections
print("Socket is listening")

while True:
    c, addr = skt.accept()
    print('Got connection from', addr)
    message = ("Thank you for connecting\n")
    c.send(message.encode()) # Transforming the text message to bytes
    c.close()
