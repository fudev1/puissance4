import tkinter as tk
from tkinter import *

y = 6
x = 7
cellTaille= 100

fenetre = tk.Tk()
fenetre.title("Puissance 4")

grille = [[0 for _ in range(x)] for _ in range(y)]

Frame1 = Frame(fenetre, relief=tk.SOLID)
Frame1.pack(side=tk.LEFT, padx=5, pady=5)

canvas = Canvas(Frame1, width=x * cellTaille, height=y * cellTaille, bg='blue')

canvas.pack()

player1 = StringVar()
player1.set("Joueur 1")
entry1 = Entry(fenetre, textvariable=player1, width=30)
entry1.pack()

player2 = StringVar()
player2.set("Joueur 2")
entry2 = Entry(fenetre, textvariable=player2, width=30)
entry2.pack()

def tab():
    for row in range(y):
        for col in range(x):
            x1 = col * cellTaille
            y1 = row * cellTaille
            x2 = x1 + cellTaille -10
            y2 = y1 + cellTaille -10
            canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill='white')

tab()

fenetre.mainloop()