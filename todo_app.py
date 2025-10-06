import tkinter as tk
from tkinter import ttk, messagebox

class TodoApp:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("Takenlijst")

        self.task_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.task_var, width=30).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(root, text="Voeg toe", command=self.add_task).grid(row=0, column=1, padx=10, pady=10)

        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ttk.Button(root, text="Verwijder geselecteerde", command=self.remove_task).grid(row=2, column=0, columnspan=2, pady=10)

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_var.set("")
        else:
            messagebox.showwarning("Leeg veld", "Voer een taak in.")

    def remove_task(self):
        selected = self.listbox.curselection()
        if selected:
            self.tasks.pop(selected[0])
            self.update_listbox()
        else:
            messagebox.showwarning("Geen selectie", "Selecteer een taak om te verwijderen.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for t in self.tasks:
            self.listbox.insert(tk.END, t)