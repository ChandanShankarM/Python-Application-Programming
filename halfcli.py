#CLIENT


from socket import *
server_name='localhost'
server_port=2001
client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect((server_name,server_port))

while True:
    sen=input(">>>")
    client_socket.send(sen.encode())
    msg=client_socket.recv(1024)
    print(">>>",msg.decode())
    if sen=='z':
        client_socket.close()



























