import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 9500                
s.bind((host, port))        

s.listen(5)                 

c, addr = s.accept() 

# Receives message from client
message = c.recv(9500)

# Decodes the client message & verifies it's what we're looking for
if message.decode() == "Hello":

    # Establish connection with client.
   c.send("Hi".encode())
   c.close()    
   
else:
    c.send("Goodbye".encode())
    c.close()