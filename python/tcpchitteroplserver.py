 #!/usr/bin/env python


import socket
import chitteroplbasic as chitter

TCP_IP = '127.0.0.1'
TCP_PORT = 5012
BUFFER_SIZE = 1024
MESSAGE = ""



theGame = chitter.ChitterOPLGraph('conv01');

theGame.load_twine_file('chitteropl04.html')

# theGame.print_tables();
# conv.save_json("guessmynumber.json")
# theGame.reset()



recieved_int = 0
recieved_string = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
print("listening...")
s.listen(1)
 
conn, addr = s.accept()
print ('Connection address:', addr)
while True:

    
    #process player input
    try:
     data = conn.recv(BUFFER_SIZE)
    except ConnectionResetError:
    
     print("connection reset, listening...")
     conn, addr = s.accept()
     print ('Connection address:', addr)
    except ConnectionAbortedError:
     print("connection aborted, listening...")
     conn, addr = s.accept()
     print ('Connection address:', addr)
     
    #process application messages
    recieved_string = data.decode('utf-8')
    if(recieved_string == "shutdownserver"):
        print("shutting down server...")
        break;
            

    print ("r: ", recieved_string)
    theGame.process_input(recieved_string)
    #recieved_string = "" #consumer string so it doesn't loop around  
    
    #process game requests
    theGame.turn()
    
    #display gamestate
    MESSAGE = theGame.current_message()
    print ("s: ", MESSAGE)
    conn.send(MESSAGE.encode('utf-8'))
    
   
    
    
conn.close()











