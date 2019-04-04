#coding utf-8

#mettre une majuscule lors de l'importation de Tkinter sinon ne marche pas 
from Tkinter import * 

fenetre =  Tk()
fenetre.geometry('500x500')
fenetre.title("iencli")


#organisation de la fenetre en forme de volet grace a panedwindow

p = PanedWindow(fenetre, orient = HORIZONTAL)
p.pack(side=TOP, expand=Y, padx=1, pady=1, borderwidth=GROOVE)
p.add(Label(p, text='Le tree sera ici', background='red', anchor=W ))
p.pack()
#premiere partie connexion


fenetre.mainloop()

