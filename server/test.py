import socket

# https://   www.         geeksforgeeks.org   /socket-programming-python/
# protocol , subdomain    domain                path -> functions


ip = socket.gethostbyname('www.google.com')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect((ip, 80))
