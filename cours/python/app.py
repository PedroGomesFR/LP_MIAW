# app.py
import tkinter as tk

# Crée la fenêtre principale
root = tk.Tk()
root.title("Mon application Tkinter")

# Crée un label avec une variable de contrôle
label_text = tk.StringVar()
label_text.set("Bienvenue dans mon application!")
label = tk.Label(root, textvariable=label_text)
label.grid(row=0, column=0, padx=20, pady=20)

# Crée un bouton
def on_click():
    label_text.set("Vous avez cliqué sur le bouton!")
button = tk.Button(root, text="Cliquez ici", command=on_click)
button.grid(row=1, column=0, padx=20, pady=20)

# Définit la taille de la fenêtre
root.geometry("800x600")

# Lance la boucle principale
root.mainloop()