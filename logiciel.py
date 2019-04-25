#coding: utf-8

from Tkinter import * 


	

HEIGHT = 600
WIDTH = 800

root = Tk()

#taille fenetre
canvas = Canvas(root, height = HEIGHT, width = WIDTH )
canvas.pack()

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
Button_connexion = Button(Framefirst, text = 'Connexion', font = 20)
Button_connexion.place(relx = 0.69, relwidth= 0.3, relheight = 1)

######################    Deuxieme Frame    #######################

Deuframe = Frame(root, bg = 'pink', bd = 6 )
Deuframe.place(relx = 0.5 , rely = 0.255, relwidth= 0.75, relheight = 0.7 , anchor='n')

#Demande l'option au client 

Option = Label(Deuframe, text = "Choisissez l'option désirée :",bg = 'pink', fg = 'black', font = 20)
Option.place(relx = 0.33, rely = 0)

#Les différentes options 

DownloadFill = Button(Deuframe, text = 'Download', command = Clic)
DownloadFill.place(relx = 0.3 , rely = 0.2, relwidth= 0.2, relheight = 0.1)

UploadFill = Button(Deuframe, text = 'Upload')
UploadFill.place(relx = 0.5 , rely = 0.2, relwidth= 0.2, relheight = 0.1)

#Afiichage des labels a la demande du client


root.mainloop()