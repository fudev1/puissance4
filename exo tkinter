import tkinter as tk
from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="Puissance 4", bg="white")
label.pack()
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()
value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable="Entrer votre nom: ", width=40)
entree.pack()

Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=100, pady=100)

Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)

Frame3 = Frame(fenetre, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=tk.BOTTOM, padx=5, pady=5)

Label(Frame1, text="La grille").pack(padx=300, pady=200)
Label(Frame2, text="Les scores").pack(padx=70, pady=150)
Label(Frame3, text= "Le tour").pack(padx=100, pady=40)


fenetre.mainloop()

