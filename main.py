# Takenlijst Project
#
# Dit is een eenvoudige takenlijst-applicatie in Python met Tkinter.
#
# ## Gebruik
#
# - Start het programma met `python main.py`
# - Voeg taken toe en verwijder ze via de interface
#
# ## Bestanden
#
# - `main.py`: Start het programma
# - `todo_app.py`: Bevat de logica en GUI

from todo_app import TodoApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

