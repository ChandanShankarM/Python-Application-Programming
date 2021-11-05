#HALF DUPLEX


#SERVER

from socket import *
server_port=2001
server_socket=socket(AF_INET,SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(1)
print("Welcome the server is ready")
c_socket,address=server_socket.accept()
while True:
    sen=c_socket.recv(1024).decode()
    print(">>>",sen)
    msg=input(">>>")
    c_socket.send(msg.encode())
    if msg=='z':
        c_socket.close()
        

















