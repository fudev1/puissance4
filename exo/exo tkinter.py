import tkinter as tk
from tkinter import Frame, Canvas


y = 6
x = 7
cell_size= 100

fenetre = tk.Tk()
fenetre.title("Puissance 4")


board = [[0 for _ in range(x)] for _ in range(y)]


Frame1 = Frame(fenetre, relief=tk.GROOVE)
Frame1.pack(side=tk.LEFT, padx=100, pady=100)

Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)




canvas1 = Canvas(Frame1, width=x * cell_size, height=y * cell_size, bg='blue')
canvas2 = 
canvas3 = 
canvas.pack()


def draw_board():
    for row in range(y):
        for col in range(y):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            canvas1.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill='white')


draw_board()


fenetre.mainloop()


fenetre.mainloop()

