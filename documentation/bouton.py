from tkinter import Tk, Button

fenetre = Tk()

"""
# Créer un bouton
# ➡️ Button(fenetre, text="Click me") = Créer un bouton et lui attribuer le texte "Click me"
# 🟡 Button() peut prendre plusieurs paramètres (bg, fg, font, height)
# 🟡 command = fonction à exécuter lorsque le bouton est cliqué 
# 🟡 command peut prendre plusieurs arguments, comme : 
# - fenetre.quit() pour quitter la fenêtre
# - une fonction personnalisée
"""

bouton = Button(fenetre, text="Click moi")
bouton2 = Button(fenetre, text="Quitter", command=fenetre.quit)

bouton.pack()
bouton2.pack()

fenetre.mainloop()