#!/usr/bin/python           # This is server1.py file

from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",4032))
s.listen(5)
while True:
 c,a = s.accept()
 print "Received connection from", a
 c.send("Hello %s\n" % a[0])
 c.close()
