import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 9500                

s.connect((host, port))

s.send('Hello'.encode())

# Receives the message sent via the server depending on the message
# the client initially sent.
message = s.recv(9500)

print (message.decode())
s.close()