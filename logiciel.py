#coding utf-8

from tkinter import * 

HEIGHT = 500
WIDTH = 500

root = Tk()

#taille fenetre
canvas = Canvas(root, height = HEIGHT, width = WIDTH )
canvas.pack()

#Frame permet de créer des frames a l'interieur d'une fenetre
Frame = Frame(root, bg = 'pink', cursor= 'arrow')
Frame.place(relx = 0.5 , rely = 0.4 , relwidth= 0.75, relheight = 0.1 , anchor='n')

#Titre et saisi de l'identifiant 
IDlab = Label(Frame,text = 'Identifiant',bg='pink' ,fg = 'black')
IDlab.place(relx = 0.048, rely = 0.1 , relwidth= 0.2, relheight = 0.4)

IdEntry = Entry(Frame, text = 'ex : Paula' , fg = 'black')
IdEntry.place(relx = 0.01, rely = 0.5 , relwidth= 0.3, relheight = 0.3)

#Titre et saisi du mot de passe
MDPlab = Label(Frame, text= 'Mot de passe', bg='pink' ,fg = 'black')
MDPlab.place(relx = 0.4, rely = 0.1 , relwidth= 0.2, relheight = 0.4)

MDPEntry = Entry(Frame)
MDPEntry.place(relx = 0.355, rely = 0.5 , relwidth= 0.3, relheight = 0.3)

#Bouton entrer

Button = Button(Frame, text = 'Connexion', font = 40)
Button.place(relx = 0.69, relwidth= 0.3, relheight = 1)

root.mainloop()