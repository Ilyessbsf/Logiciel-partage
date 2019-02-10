#coding utf-8

import socket, os

"""importation du protocole TCP(plus lent mais plus sur) avec SOCKET_STREAM"""
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket.bind(('', 29876)) #liaison point de communication defini par une adresse et un port
os.system('pause')
while True:
	socket.listen(5) #fonction listen() permet de mettre un socket en attente de connexion, ici durant 5s
	client, address = socket.accept() #fonction accept() permet la connexion en acceptant un appel
	print "{} conected".format( address ) 

	response = client.recv(255)
	if response != "":
			print response

print "Close"
os.system('pause')
client.close()
socket.close()
