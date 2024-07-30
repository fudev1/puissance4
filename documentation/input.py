from tkinter import Tk, StringVar, Entry

fenetre = Tk()

"""
# Créer une entrée de texte
# ➡️ StringVar() = Créer une variable de type String
# ➡️ Entrée(fenetre, textvariable=string, width=30) = Créer une entrée de texte et lui attribuer la variable string
"""

value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=string, width=30)
entree.pack()

fenetre.mainloop()