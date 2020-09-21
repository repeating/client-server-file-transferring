import socket                   # Import socket module
import sys
import os

# Create a socket object
s = socket.socket()

# get the host, port and filename from the command
host = sys.argv[2]     
port = sys.argv[3]              
filename = sys.argv[1]

# print the name of the file
print(filename)

# coonecnt to the server
s.connect((host, int(port)))

# send file name to the server
s.sendall(filename.encode())

f = open(filename,'rb')

# send the data inside the file
data = f.read(1024)
size = os.stat(filename).st_size
sent = 0
while (data):
    s.send(data)
    data = f.read(1024)
    sent += 1024
    print('Sending..%{}'.format(min(int(sent*100/size), 100)))
f.close()

# finish the process
print(filename,'successfully sent.')
s.shutdown(socket.SHUT_WR)
s.close()
