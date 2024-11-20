import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pandas as pd
import json

class ExcelToJsonViewer:
    def __init__(self, master):
        self.master = master
        master.title("Afficheur Excel to JSON")
        master.geometry("600x400")

        # Bouton de chargement de fichier
        self.load_button = tk.Button(master, text="Charger fichier Excel", command=self.load_excel_file)
        self.load_button.pack(pady=20)

        # Zone de texte pour afficher le contenu JSON
        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=70, height=15)
        self.text_area.pack(pady=10)

    def load_excel_file(self):
        file_path = filedialog.askopenfilename(
            title="Sélectionnez un fichier Excel",
            filetypes=[("Fichiers Excel", "*.xlsx *.xls")]
        )

        if file_path:
            try:
                # Charger le fichier Excel
                df = pd.read_excel(file_path)

                # Vérifier si la colonne 'DayDate' existe
                if 'DayDate' not in df.columns:
                    messagebox.showerror("Erreur", "La colonne 'DayDate' n'existe pas dans le fichier Excel.")
                    return
                
                # Générer la colonne CleWeb à partir de la colonne DayDate
                df['CleWeb'] = self.generate_cleweb(df['DayDate'])

                # Convertir le DataFrame en JSON
                json_content = df.to_json(orient='records', force_ascii=False, indent=2)

                # Afficher le JSON dans la zone de texte
                self.text_area.delete(1.0, tk.END)  # Effacer le texte précédent
                self.text_area.insert(tk.END, json_content)  # Afficher le contenu JSON

            except Exception as e:
                messagebox.showerror("Erreur", str(e))

    def generate_cleweb(self, day_dates):
        return [f"{date.strftime('%Y%m%d')}-{str(i+1).zfill(4)}" for i, date in enumerate(day_dates)]

def main():
    root = tk.Tk()
    app = ExcelToJsonViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()