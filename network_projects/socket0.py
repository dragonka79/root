""" 
Creating a socket and connecting to a server 
"""

import socket
import sys

try:
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket is created successfully')
except socket.error as err:
    print(f'Socket creation failed with error {err}')
 
def_port = 443  

try:
    host_ip = socket.gethostbyname('www.github.com') # Getting the IP of the FQDN 
except socket.gaierror: # In case of a problem with the DNS
    print("Name resolution failed")
    sys.exit()
    
# Connecting to the server
skt.connect((host_ip, def_port))
print(f"Socket is connected to Github on IP {host_ip} on port {def_port}")

# print(ip)
