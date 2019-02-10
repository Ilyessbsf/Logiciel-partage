#coding utf-8

import socket, os 

hote = "localhost"
port = 29876
os.system('pause')
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket.connect((hote, port))
print "Connection on {}".format(port)

socket.send("Hey tat's just a test for executing my program")

print "close"
os.system('pause')
socket.close() 
