# view.py
import tkinter as tk
from tkinter import filedialog, ttk

class TrombiView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Boutons et labels
        ttk.Button(main_frame, text="Charger Photos", 
                  command=self.controller.load_photos).grid(row=0, column=0, pady=5)
        
        ttk.Button(main_frame, text="Charger Liste Étudiants", 
                  command=self.controller.load_students).grid(row=1, column=0, pady=5)
        
        ttk.Button(main_frame, text="Sélectionner Template", 
                  command=self.controller.select_template).grid(row=2, column=0, pady=5)
        
        ttk.Button(main_frame, text="Générer Trombinoscope", 
                  command=self.controller.generate_trombi).grid(row=3, column=0, pady=5)

        # Zone de status
        self.status_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.status_var).grid(row=4, column=0, pady=10)

    def update_status(self, message):
        self.status_var.set(message)