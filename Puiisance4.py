import tkinter as tk

def place_token(row, col):
    # Logique pour placer un jeton dans la colonne
    pass

def reset_game():

    # Réinitialiser le tableau de jeu
    for row in range(6):
        for col in range(7):
            buttons[row][col].config(text="", state=tk.NORMAL)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu Puissance 4")

# Création du cadre
frame = tk.Frame(root)
frame.pack()

# Créeation de la grille de boutons 6x7
buttons = []
for row in range(6):
    row_buttons = []
    for col in range(7):
        button = tk.Button(frame, text="", width=10, height=4, command=lambda r=row, c=col: place_token(r, c))
        button.grid(row=row, column=col)
        row_buttons.append(button)
    buttons.append(row_buttons)

# Ajout des boutons Réinitialiser et Quitter
reset_button = tk.Button(root, text="Réinitialiser", command=reset_game)
reset_button.pack(side=tk.LEFT, padx=20, pady=20)

quit_button = tk.Button(root, text="Quitter", command=root.quit)
quit_button.pack(side=tk.RIGHT, padx=20, pady=20)

# Lancer la boucle principale de l'interface graphique
root.mainloop()
