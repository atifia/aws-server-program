import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 4032                # Reserve a port for your service.

s.connect((52.57.29.249, 4032))
print s.recv(1024)
s.close                     # Close the socket when done
