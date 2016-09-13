#!/usr/bin/python           # This is client1.py file

from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(("52.57.29.249",4032)) # Connect
s.send("Hello from client !") # Send request
data = s.recv(10000) # Get response
s.close()
