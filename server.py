import socket                   
import os.path
from time import sleep

# Create a socket object
port = 8080                  
s = socket.socket()             
ip = socket.gethostbyname(socket.gethostname())    

# Bind to the port
s.bind((ip, port))

# Now wait for client connection.
s.listen(5)                     
print('The server is running on the private ip:', ip)	
print('Listening on port:', port)
print('-----------')

while True:
     # Establish connection with client.
    c, addr = s.accept()    
    
    # receive the file name
    filename = c.recv(1600)
    filename = filename.decode()
    
    # check if there are files with the same name
    write_name = filename
    if os.path.exists(write_name): 
        i = 1
        while True:
            NAME, FORMAT = filename.split('.')
            write_name = NAME + '_copy' + str(i) + '.' + FORMAT
            if not os.path.exists(write_name):
                break
            i += 1

    f = open(write_name,'wb')
    
    # receive data 
    print('Connection from:', addr)
    print('Receiving..')
    
    data = c.recv(1024)
    while (data):
        f.write(data)
        data = c.recv(1024)
    f.close()
    sleep(0.05)
    print('Done!')
    
    # close the socket
    c.shutdown(socket.SHUT_WR)
    c.close()
