#coding: utf-8

from tkinter import * 
from tkinter.messagebox import *
import socket, os, subprocess, pickle, codecs

def Download_ig():
	#Afiichage des labels a la demande du client
	MessageDown = Label(Deuframe, text = "Veuillez écrire le nom du fichier que vous voulez télécharger : ", bg = 'pink', fg = 'black', font = 15)
	MessageDown.place(relx = 0.16 , rely = 0.34, relwidth= 0.72, relheight = 0.2)
	
	EntryDown = Entry(Deuframe)
	EntryDown.place(relx = 0.36 , rely = 0.5, relwidth= 0.3, relheight = 0.09)

	Button_Valider_down = Button(Deuframe, text = "Valider", command = download)
	Button_Valider_down.place(relx = 0.36 , rely = 0.6, relwidth= 0.3, relheight = 0.09)

def Upload_ig():
	#Afiichage des labels a la demande du client
	MessageUp = Label(Deuframe, text = "Veuillez écrire le nom du fichier que vous voulez insérer : ", bg = 'pink', fg = 'black', font = 15)
	MessageUp.place(relx = 0.16 , rely = 0.34, relwidth= 0.7, relheight = 0.2)

	EntryUp = Entry(Deuframe)
	EntryUp.place(relx = 0.36 , rely = 0.5, relwidth= 0.3, relheight = 0.09)

	Button_Valider_up = Button(Deuframe, text = "Valider", command = upload)
	Button_Valider_up.place(relx = 0.36 , rely = 0.6, relwidth= 0.3, relheight = 0.09)

def deconnexion_ig():
	#message deco client
	showinfo("Déconnexion", "Vous avez été déconnectés avec succès !")
	root.destroy()

def connection(hote, port):

	connection_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		connection_server.connect((hote, port))
	except:
		print("[*] Hôte inéxistant ")
		os.system("pause")
		os.system("exit")
	return connection_server

def auth():
	"""
		Envoie des identifiants et recup de la reponse
		renvoie un booléen pour savoir si on continue ou non
	"""
	global server, connectivity,echec_connection, output_str

	username = get_username()
	password = get_password()

	# On dump la list pour pouvoir l'envoyer a travers le socket
	id_ = [username, password]
	id_dump = pickle.dumps(id_)
	server.send(id_dump)
	#On recupere une listeen retour qu'on dé-dump
	log_state = server.recv(2048)
	log_state = pickle.loads(log_state)

	if log_state[0] == "Success": # La liste contient le mot clef "Success" -> on est auth.
		print("{} a autorisé une connection".format(server))
		# On récup l'arbo
		codecs.register_error('replace_with_space', lambda e: (u'',e.start + 1)) # On remplace les potentiels erreurs par des espaces
		output_str = log_state[1].decode("utf-8", errors='replace_with_space')
		connectivity = True # True -> on peut continuer

	elif log_state[0] == "Fail": # La liste contient le mot clef "Fail" -> on est pas auth.
		print("Le serveur indique : {}".format(log_state[1]))

		echec_connection = Tk()
		echec_connection.title('Echec de la connexion')
		label_echec = Label(echec_connection, text="Le serveur indique : {}".format(log_state[1])).grid(row=0, column=0)
		button_quit = Button(echec_connection, text="quitter", command=destroy_auth_error).grid(row=1, column=1)


		connectivity = False # False -> on est déconnécté

def download():
	"""
		Donne au serveur l'ordre d'envoyer un fichier
	"""
	global server
	folder = str(get_folder())
	filename = str(get_filename())
	print(folder)

	# on crée le chemin absolue
	path = "partage/"+folder +"/"+filename
	print(path)
	data = ["download", path]
	#on dump la liste
	data = pickle.dumps(data)
	server.send(data)

	content = server.recv(2**30) # Reception du conenue du fichier

	if content == b"unknown":
		print("Fichier inéxistant")
	else:
		with open(filename, "wb") as f: # Creation d'un fichier similaire
			print(content)
			f.write(content)
			f.close()

def upload():
	"""
	"""
	global server
	path, target = get_upload_path()
	path_split = path.split('/')
	filename = path_split[-1]
	data = ["upload", filename, 0, target]
	print(path, target, filename)
	# On verifie que le fichier existe
	try:
		with open(path, "rb") as f:
			content = f.read()
			data[2] = content
			
		#on dump la liste
		data = pickle.dumps(data)
		server.send(data)
		print("Le fichier a été copié avec succès")
	except:
		print("Le fichier n'éxiste pas .")



# Fonctions pour récuperer les entrés de l'it graphique

def get_username():
	return IdEntry.get()

def get_password():
	return MDPEntry.get()

def get_folder():
	return entry_folder_dl.get()
 
def get_filename():
	return entry_filename.get()

#En cas d'erreur, détruire toute les fenetres

def destroy_auth_error():
	echec_connection.destroy()
	interface_client.destroy()

def destroy_download_error():
	pass
		
def arbo():
	arbo_window = Tk()
	label_arbo = Label(arbo_window, text=output_str).grid(row=0, column=0)
	arbo_window.mainloop()

def get_upload_path():
	path = askopenfilename()
	target = entry_folder.get()
	return path, target


if __name__ == "__main__":


	#On se connecte au server
	server = connection("localhost", 9999)

#################################### Interface graphique ############################################
HEIGHT = 600
WIDTH = 800

root = Tk()
#taille fenetre
canvas = Canvas(root, height = HEIGHT, width = WIDTH )

canvas.pack()

############ Menu ###################
#menubar = Menu(interface_client)
#menubar.add_command(label="Arbo", command=arbo)
#interface_client.config(menu=menubar)

############################ fond ###############################

#background_image = PhotoImage(file='logo_6.png')
#backgroung_label = Label(root, image=background_image)
#backgroung_label.place(relwidth = 1 , relheight = 1)

########################### Frame #######################################

#Frame permet de créer des frames a l'interieur d'une fenetre
Framefirst = Frame(root, bg = 'pink', bd = 5)
Framefirst.place(relx = 0.5 , rely = 0.1 , relwidth= 0.75, relheight = 0.1 , anchor='n')

#Titre et saisi de l'identifiant 
IDlab = Label(Framefirst,text = 'Identifiant',bg='pink' ,fg = 'black')
IDlab.place(relx = 0.048, rely = 0.1 , relwidth= 0.2, relheight = 0.4)

IdEntry = Entry(Framefirst, text = 'ex : Paula' , fg = 'black')
IdEntry.place(relx = 0.01, rely = 0.5 , relwidth= 0.3, relheight = 0.3)

#Titre et saisi du mot de passe
MDPlab = Label(Framefirst, text= 'Mot de passe', bg='pink' ,fg = 'black')
MDPlab.place(relx = 0.4, rely = 0.1 , relwidth= 0.2, relheight = 0.4)

MDPEntry = Entry(Framefirst)
MDPEntry.place(relx = 0.355, rely = 0.5 , relwidth= 0.3, relheight = 0.3)

#Bouton entrer
Button_connexion = Button(Framefirst, text = 'Connexion', font = 20, command = auth)
Button_connexion.place(relx = 0.69, relwidth= 0.3, relheight = 1)

######################    Deuxieme Frame    #######################

Deuframe = Frame(root, bg = 'pink', bd = 6 )
Deuframe.place(relx = 0.5 , rely = 0.255, relwidth= 0.75, relheight = 0.7 , anchor='n')

#Demande l'option au client 

Option = Label(Deuframe, text = "Choisissez l'option désirée :",bg = 'pink', fg = 'black', font = 20)
Option.place(relx = 0.3, rely = 0, relwidth = 0.4, relheight = 0.1)

#Les différentes options 

DownloadFill = Button(Deuframe, text = 'Download', command = Download_ig)
DownloadFill.place(relx = 0.3 , rely = 0.2, relwidth= 0.2, relheight = 0.1)

UploadFill = Button(Deuframe, text = 'Upload', command = Upload_ig)
UploadFill.place(relx = 0.5 , rely = 0.2, relwidth= 0.2, relheight = 0.1)

# Bouton pour deconnexion

Button_deconnexion = Button(Deuframe, text = "Se déconnecter", font = 14, command = deconnexion_ig)
Button_deconnexion.place(relx = 0.7 , rely = 0.9, relwidth= 0.3, relheight = 0.09)





root.mainloop()