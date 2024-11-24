import socket

# https://   www.         geeksforgeeks.org   /socket-programming-python/
# protocol , subdomain    domain                path -> functions


s = socket.socket()

ip = '127.0.0.1'

s.connect((ip, 1213))

print(s.recv(1024).decode())
