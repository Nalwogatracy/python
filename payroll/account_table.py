import tkinter as tk
from tkinter import ttk
import sqlite3

class DisplayAccountsApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Display Accounts")
        self.geometry("1366x768+0+0")

        style = ttk.Style()
        style.configure("Treeview.Heading", foreground="royal blue", background="black", font=('Times New Roman', 12))
        #style.configure("Treeview.Heading", background="dark blue", foreground="white", font=('Times New Roman', 12))
        style.configure("Treeview", font=('Times New Roman', 12))

        self.tree = ttk.Treeview(self, columns=("Employee ID", "Name", "Responsibility", "Basic Salary", "Taxes", "Allowances", "Gross Pay", "Net Pay"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("Employee ID", text="Employee ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Responsibility", text="Responsibility")
        self.tree.heading("Basic Salary", text="Basic Salary")
        self.tree.heading("Taxes", text="Taxes")
        self.tree.heading("Allowances", text="Allowances")
        self.tree.heading("Gross Pay", text="Gross Pay")
        self.tree.heading("Net Pay", text="Net Pay")

        self.tree.pack(fill="both", expand=True)

        self.populate_treeview()

    def populate_treeview(self):
        connection = sqlite3.connect("registration.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM account")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", text=row[0], values=row[1:])
        connection.close()

if __name__ == "__main__":
    app = DisplayAccountsApp()
    app.mainloop()
