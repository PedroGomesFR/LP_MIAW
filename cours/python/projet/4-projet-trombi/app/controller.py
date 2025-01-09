# controller.py
from tkinter import filedialog
import os

class TrombiController:
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view

    def load_photos(self):
        directory = filedialog.askdirectory()
        if directory:
            count = self.model.load_photos(directory)
            self.view.update_status(f"{count} photos chargées")

    def load_students(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])
        if file_path:
            count = self.model.load_students(file_path)
            self.view.update_status(f"{count} étudiants chargés")

    def select_template(self):
        template = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
        if template:
            self.model.template_path = template
            self.view.update_status("Template sélectionné")

    def generate_trombi(self):
        if not all([self.model.photos, self.model.students, self.model.template_path]):
            self.view.update_status("Erreur: Données manquantes")
            return

        output_path = filedialog.asksaveasfilename(
            defaultextension=".docx",
            filetypes=[("Word files", "*.docx")])
        
        if output_path:
            try:
                self.model.create_trombi(self.model.template_path, output_path)
                self.view.update_status("Trombinoscope généré avec succès!")
            except Exception as e:
                self.view.update_status(f"Erreur: {str(e)}")