 #!/usr/bin/env python

import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5012
BUFFER_SIZE = 1024
MESSAGE = "reset" 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


user_input = ""

while True:

    user_input = ""
    user_input = input();
    MESSAGE = user_input


    # do application level stuff
    if(user_input == "shutdownserver"):
        s.send("shutdownserver".encode('utf-8'))
        time.sleep(2)
        break

    # this doesn't work right
    # if(user_input == "logout"):
    #     break
        
        
     
    #if the user enters nothing
    if(len(MESSAGE) == 0):
        MESSAGE = "0"

    s.send(MESSAGE.encode('utf-8'))
    print('s: ' + MESSAGE);
    
    
    data = s.recv(BUFFER_SIZE)
    print('r: ' + str(data))



s.close()

print ("done...")

