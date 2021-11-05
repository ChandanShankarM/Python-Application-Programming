'''
#Networking
#client server:
#client : any h/w or s/w request for something
#server : any h/w or s/w responds to request

#server
#waits forever so that it respond to the client
#while true:
        accept the request()
        open the connection()
        while the connection still exists()
                receive()
                respond()
close connection()

#client:
#get_the_server_add()
request for the connection()
while connected()
    send request()
    get response()
close the connection()

# ATM:
#accept the card
#ask what you want to do
#serve you
#thank you
#close the card and blink
#waits for another card

# 1-------2
#communication channel
#cable
#socket(communication endpoints): endpoints of a bidirectional communication channel
#socket may communicate within process,b/w process,on the same machine or on the different machine
# library-socket()
'''
import socket

'''
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)
print(hostname)
print(ip)

#socket.socket(s_family,s_type,protocol=0)
#s_family
#AF_UNIX-(used to communicate b/w process on same m/c)
#AF_INET-(ipv4)
#s_type
#SOCK_STREAM-TCP.............................................
#SOCK_DGRAM-UDP(connection less)


#server methods:
#s.bind-used to bind the addresses of hostname and it's port number to the socket  s.bind(hostname,port number)
#s.listen()-starts TCP listener
#s.accept()-accept the client connection


#client method:
#s.connect()-initiate the connection


#general methods:
#s.recv()-initiate receiving TCP messages
#s.send()
#s.recvfrom(): receive UDP messages
#s.sendto(): transmit UDP messages
#s.close(): close the socket


lst=['www.pes.edu','home','www.python.org','college','www.google.com','www.abc.com']
for host in lst:
    try:
            print(host,socket.gethostbyname(host))
    except socket.error as msg:
            print(host,":",msg)
            

#gethostbyname_ex()-for further info
lst=['www.pes.edu','home','www.python.org','college','www.abc.com']
for host in lst:
    print(host)
    try:
            hostname,aliases,address=socket.gethostbyname_ex(host)
            print("hostname",hostname)
            print("Aliases",aliases)
            print("Address",address)
    except socket.error as msg:
            print("ERROR",msg)
'''

#port: 0-65535
#reserved ports 0-1023
#http-80
#https-443
#smtp-25
#ftp-21

from urllib.parse import urlparse

'''
url_lst=['http://www.python.org','https://www.mybank.com','ftp://prep.ai.mit.edu','http://pes.edu','smtp://mail.example.com']
for url in url_lst:
    parsed_url=urlparse(url)
    port=socket.getservbyname(parsed_url.scheme)
    print(parsed_url.scheme,port)
'''


#getaddrinfo()

#server addresses.
# converts the basic address of a service in to list of tuple
'''
def get_info(pre_info):
        return dict((getattr(socket,n),n)
        for n in dir(socket)
        if n.startswith(pre_info))
        
families=get_info('AF_')
types=get_info('SOCK_')
protocols=get_info('IPPROTO_')


for i in socket.getaddrinfo('www.pes.edu','http'):
    family,socktype,proto,canonname,sockadd=i       #unpack
    print("family",family)
    print("socktype",socktype)
    print("protocol",proto)
    print("canonical name",canonname)
    print("address",sockadd)

#print(families,types,protocols)
'''

'''
#server:

s=socket.socket()
host=socket.gethostname()
port=25110
s.bind((host,port)) #binds the address to the socket
s.listen(1)
while True:
    c,addr=s.accept()
    print("got the connection")
    output="thank you for connecting"
    c.sendall(output.encode('utf-8'))
c.close()
'''
#UDP
#Half duplex chat
#Full duplex chat
#solving problems

#UDP-user datagram protocol
#Ip

#Properties of UDP
#connection less
#unreliable
#order may not be same
#faster transfer
#header size is small
#overhead(no error checking) is less

#server-UDP
#create socket
#bind(host name,port)
#recieve the request
#send the response


'''
local="127.0.0.1"
local_port=20012
buffersize=1024

msg_server="hey udp client"
bytesTosend=str.encode(msg_server)

socket_1=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
socket_1.bind((local,local_port))
print("udp server")
while(True):
    byteaddresspair=socket_1.recvfrom(buffersize)
    msg=byteaddresspair[0]
    address=byteaddresspair[1]
    print("msg from client",msg)
    print("address from client",address)
    socket_1.sendto(bytesTosend,address)



'''
host='localhost'
port=20000
data = open("file_created_client.txt", 'r')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
line = data.readline()
while(line):
    bdata = line.encode()
    line = data.readline()
    s.send(bdata)
s.close()
'''

'''
hostname = '' #use available interface
port_name = 20000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((hostname, port_name))

count = 0 #If more than file then counter is required else it is not required
while True:
    s.listen(1)
    connection, address = s.accept()
    print('Connection:',connection)
    print('We are connected to this by Address:', address)
    fp = open('server_created_file.txt', 'w') #Make sure if we use binary file then mention extension
    count += 1
    while True:
        msg = connection.recv(2048)
        if(msg):
            fp.write(msg.decode())
            print(msg.decode())
        else:
            connection.close()
            fp.close()
            break
'''

'''
client:

from socket import *
c=socket(AF_INET,SOCK_STREAM)
host=gethostname()
port=12345
c.connect((host,port))
print("Connection has been made with server")
while(True):
 i=input("Client:")
 c.send(i.encode('utf-8'))
if i =="exit":
 c.close()
break
print("\t\t\tServer:",c.recv(1024).decode('utf-8'))


server:


from socket import *
s=socket(AF_INET,SOCK_STREAM)
host=gethostname()
port=12345
s.bind((host,port))
s.listen(1) 
print("Server waiting for connection")
c,addr=s.accept()
print("Server has made connection with", addr)
while True:
 i=c.recv(1024).decode('utf-8')
print("\t\t\tClient: ",i)
if i=="exit":
 s.close()
break
 i=i[::-1]
print("Server: ",i)
 c.sendall(i.encode('utf-8'))
'''
