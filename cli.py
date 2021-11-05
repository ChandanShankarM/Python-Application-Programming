import socket
'''
s=socket.socket()
host=socket.gethostname()
port=25110
s.connect((host,port))
s.send(input().encode('utf-8'))
print(c.recv(1024).decode('utf-8'))
print(s.recv(1024))
s.close()
'''
'''
msgfromclient="hello udp server"
bytesTosend=str.encode(msgfromclient)
serveraddressport=("127.0.0.1",20012)
buffersize=1024

udpclientsocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
udpclientsocket.sendto(bytesTosend,serveraddressport)
msgfromserver=udpclientsocket.recvfrom(buffersize)
print("msg from server",msgfromserver[0])
'''


















