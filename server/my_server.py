import socket


s = socket.socket()


s.bind(('127.0.0.1', 1213))
s.listen(5)

print("Server Is Ready For Answer to Requests !!! ")


while True:
    s_obj, addr = s.accept()

    print("addres of user : ", addr)
    s_obj.send('Thank you for connecting'.encode())

    s_obj.close()
    print("Closed")

    break
