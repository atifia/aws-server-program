from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(("52.57.29.249",4032))
s.listen(5)
while True:
 c,a = s.accept()
 print "Received connection from", a
 c.send("Hello %s\n" % a[0])
 c.close()
 
