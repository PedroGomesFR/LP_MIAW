# main.py
import tkinter as tk
from controller import TrombiController
from view import TrombiView
from model import TrombiModel

def main():
    root = tk.Tk()
    root.title("Générateur de Trombinoscope")
    
    model = TrombiModel()
    controller = TrombiController(model)
    view = TrombiView(root, controller)
    
    root.mainloop()

if __name__ == "__main__":
    main()