from tkinter import Tk, Label

fenetre = Tk()

"""
# Créer une étiquette
# ➡️ Label(fenetre, text="Hello World") = Créer une étiquette et lui attribuer le texte "Hello World"
# ➡️ pack() = organise et affiche les widgets en les plaçant dans la fenêtre les uns à côté des autres selon l'ordre de leur appel
"""

label = Label(fenetre, text="Hello World")
label.pack()

fenetre.mainloop()