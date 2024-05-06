import tkinter as tk
from tkinter import ttk, messagebox
# from PIL import Image, ImageTk
import sqlite3

class Register(tk.Tk):
    def __init__(self, root):
        self.root = root
        self.root.title("Pay-Roll System/Add Account")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="white")

        # self.left = ImageTk.PhotoImage(file="images/images.png")
        # left = tk.Label(self.root, image=self.left)
        # left.place(x=20, y=100, width=300, height=500)

        frame1 = tk.Frame(self.root, bg="white")
        frame1.place(x=350, y=100, width=700, height=500)

        title = tk.Label(frame1, text="Register Here", font=("times new roman", 20, "bold"), bg="white", fg="green")
        title.place(x=50, y=30)

        username = tk.Label(frame1, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="black")
        username.place(x=50, y=100)

        self.txt_username = tk.Entry(frame1, font=("times new roman", 15), bg="white", fg="black")
        self.txt_username.place(x=50, y=130, width=250)

        passwd = tk.Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        passwd.place(x=370, y=100)

        self.txt_passwd = tk.Entry(frame1, font=("times new roman", 15), bg="white", fg="black")
        self.txt_passwd.place(x=370, y=130, width=250)

        cpasswd = tk.Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        cpasswd.place(x=50, y=170)

        self.txt_cpasswd = tk.Entry(frame1, font=("times new roman", 15), bg="white", fg="black")
        self.txt_cpasswd.place(x=50, y=200, width=250)

        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TCombobox', bg="white", fg="black")
        style.map('TCombobox', fieldbackground=[('readonly', '#161B21')])

        category = tk.Label(frame1, text="Category", font=("times new roman", 15, "bold"), bg="white", fg="black")
        category.place(x=370, y=170)

        self.cmb_category = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=tk.CENTER)
        self.cmb_category.place(x=370, y=200, width=250)
        self.cmb_category['values'] = ("Select", "HR", "Accounts", "User")
        self.cmb_category.current(0)

        self.var_chk = tk.IntVar()
        chk = tk.Checkbutton(frame1, text="Agree to Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", fg="black", activebackground="#F4A950", activeforeground="#161B21", font=("times new roman", 12))
        chk.place(x=50, y=250)

        btn_register = tk.Button(frame1, text="Register Now", font=("times new roman", 13), bg="green", fg="white", activebackground="#F4A950", activeforeground="#161B21", bd=0, cursor="hand2", command=self.register_data)
        btn_register.place(x=50, y=300)

        btn_login = tk.Button(self.root, text="Go to account", font=("times new roman", 13), bg="blue", fg="white", activebackground="#F4A950", activeforeground="#161B21", bd=0, cursor="hand2", command=self.signin)
        btn_login.place(x=870, y=530, width=120)

    def signin(self):
        self.root.destroy()
        import login

    def clear(self):
        self.txt_username.delete(0, tk.END)
        self.txt_passwd.delete(0, tk.END)
        self.txt_cpasswd.delete(0, tk.END)
        self.cmb_category.current(0)

    def register_data(self):
        if self.txt_username.get() == "" or self.txt_passwd.get() == "" or self.txt_cpasswd.get() == "" or self.cmb_category.get() == "Select":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        elif self.txt_passwd.get() != self.txt_cpasswd.get():
            messagebox.showerror("Error", "Passwords are not matched", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree Terms & Conditions", parent=self.root)
        else:
            try:
                # Connect to SQLite database
                con = sqlite3.connect('registration.db')
                cur = con.cursor()
                # Create table if not exists
                cur.execute('''CREATE TABLE IF NOT EXISTS user_accounts (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT UNIQUE,
                                password TEXT,
                                category TEXT
                                )''')
                # Check if username already exists
                cur.execute("SELECT * FROM user_accounts WHERE username=?", (self.txt_username.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists with the same username. Register with another username", parent=self.root)
                else:
                    # Insert new record
                    cur.execute("INSERT INTO user_accounts (username, password, category) VALUES (?, ?, ?)",
                                (self.txt_username.get(), self.txt_passwd.get(), self.cmb_category.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                    self.clear()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

root = tk.Tk()
obj = Register(root)
root.mainloop()
