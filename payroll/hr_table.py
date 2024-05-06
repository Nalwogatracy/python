import tkinter as tk
from tkinter import ttk
import sqlite3

class EmployeeTable(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Employee Information Table")
        self.geometry("1366x768+0+0")

        self.header_frame = tk.Frame(self,relief=tk.RIDGE,bg="white")
        self.header_frame.place(x=0,y=0,width=1020,height=80)

        progressbar = ttk.Progressbar(self.header_frame, orient="horizontal", length=1020, mode="determinate", value=100)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("color.Horizontal.TProgressbar", foreground="royal blue", background="royal blue")
        progressbar.config(style="color.Horizontal.TProgressbar")
        progressbar.place(x=5, y=50)

        self.heading_label = tk.Label(self.header_frame, bg="white", fg="royal blue", text="Employee PayRoll System >>  View Employees", font=("Times New Roman", 16, "bold"))
        self.heading_label.place(x=300, y=5)

        self.sidebar = tk.Frame(self, width=150, bg="royal blue")
        self.sidebar.pack(side="left", fill="y")

        self.link_frame = tk.Frame(self.sidebar, relief=tk.RIDGE,bg="royal blue")
        self.link_frame.place(x=10,y=70,width=150,height=300)

        self.home_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Home", width=20, background="royal blue", font=("Times New Roman",  12, "bold"), anchor="w")
        self.home_button.pack(pady=2)
        self.home_button.config(cursor="hand2")

        self.workers_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Add Employee", width=20, background="royal blue", font=("Times New Roman",  12, "bold"), anchor="w" )
        self.workers_button.pack(pady=2)
        self.workers_button.config(cursor="hand2")

        self.view_employee_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="View Employees", width=20, background="royal blue", font=("Times New Roman",  12, "bold") , anchor="w", command=self.open_employee_table)
        self.view_employee_button.pack(pady=2)
        self.view_employee_button.config(cursor="hand2")

        self.delete_edit_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Delete/Edit", width=20, background="royal blue", font=("Times New Roman",  12, "bold"), anchor="w")
        self.delete_edit_button.pack(pady=2)
        self.delete_edit_button.config(cursor="hand2")

        self.create_user_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="User Account", width=20, background="royal blue", font=("Times New Roman",  12, "bold"), anchor="w", command=self.signup)
        self.create_user_button.pack(pady=2)
        self.create_user_button.config(cursor="hand2")

        self.logout_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Log-Out", width=20, background="royal blue", font=("Times New Roman",  12, "bold"), anchor="w")
        self.logout_button.pack(pady=2)
        self.logout_button.config(cursor="hand2")

        style = ttk.Style()
        style.configure("Treeview.Heading", foreground="white", background="royal blue", font=('Times New Roman', 12))
        #style.configure("Treeview.Heading", background="dark blue", foreground="white", font=('Times New Roman', 12))
        style.configure("Treeview", font=('Times New Roman', 12))

        self.tree = ttk.Treeview(self, columns=("Employee ID", "Name", "Residence", "Origin", "Email", "DOB", "Age", "Gender", "Contact", "Start Date", "Responsibilities"), style="Treeview")
        self.tree.heading("#0", text="Index")
        self.tree.heading("Employee ID", text="Employee ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Residence", text="Residence")
        self.tree.heading("Origin", text="Origin")
        self.tree.heading("Email", text="Email")
        self.tree.heading("DOB", text="DOB")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Contact", text="Contact")
        self.tree.heading("Start Date", text="Start Date")
        self.tree.heading("Responsibilities", text="Responsibilities")

        # Set column widths
        self.tree.column("#0", width=50)
        self.tree.column("Employee ID", width=100)
        self.tree.column("Name", width=150)
        self.tree.column("Residence", width=100)
        self.tree.column("Origin", width=100)
        self.tree.column("Email", width=150)
        self.tree.column("DOB", width=100)
        self.tree.column("Age", width=50)
        self.tree.column("Gender", width=80)
        self.tree.column("Contact", width=120)
        self.tree.column("Start Date", width=120)
        self.tree.column("Responsibilities", width=200)

        self.tree.pack(fill=tk.BOTH, expand=1)

        self.scrollbar_y = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.scrollbar_y.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.tree.configure(xscrollcommand=self.scrollbar_x.set)

        self.populate_table()

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_row)
        self.delete_button.pack(pady=10)

    def populate_table(self):
        connection = sqlite3.connect("registration.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        for i, row in enumerate(rows):
            self.tree.insert("", "end", text=str(i+1), values=row)

        connection.close()
    
    def delete_row(self):
        selected_item = self.tree.selection()
        if selected_item:
            employee_id = self.tree.item(selected_item[0], "text")
            connection = sqlite3.connect("registration.db")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM employees WHERE employee_id = ?", (employee_id,))
            connection.commit()
            self.tree.delete(selected_item[0])
            connection.close()
    def signup(self):
        #self.app.destroy()
        import signup
    def open_employee_table(self):
        employee_table = EmployeeTable()


if __name__ == "__main__":
    employee_table = EmployeeTable()
    employee_table.mainloop()