#!/usr/bin/python           # This is client1.py file

from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(("",4032)) # Connect
s.send("GET /index.html HTTP/1.0\n\n") # Send request
data = s.recv(10000) # Get response
s.close()
