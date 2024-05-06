import tkinter as tk
from tkinter import messagebox
import sqlite3
from hr_board import hrboardForm
from account_board import accboardForm
#from signup import Register
import webbrowser


class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("7366x680+0+0")
        self.root.config(bg="blue")

        login_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="white")
        login_frame.place(x=500, y=100, width=350, height=460)

        title = tk.Label(login_frame, text="Login", font=("times new roman", 30, "bold"), fg='blue',bg='white')
        title.place(x=0, y=30, relwidth=1)

        lbl_email = tk.Label(login_frame, text="User Name*", font=("times new roman", 15), fg='black',bg='white')
        lbl_email.place(x=50, y=100)
        self.email = tk.StringVar()

        txt_email = tk.Entry(login_frame, textvariable=self.email, font=("times new roman", 15), fg="black",bg='white')
        txt_email.place(x=50, y=140, width=250)

        lbl_pass = tk.Label(login_frame, text="Password", font=("times new roman", 15), bg="white", fg='black')
        lbl_pass.place(x=50, y=200)
        self.password = tk.StringVar()

        txt_pass = tk.Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15), bg="white", fg="black")
        txt_pass.place(x=50, y=240, width=250)

        btn_login = tk.Button(login_frame, command=self.login, text="LogIn", font=("times new roman", 15), bg="blue", activebackground="#EC4D37", fg="white", activeforeground="#1D1B1B", cursor="hand2")
        btn_login.place(x=50, y=300, width=100, height=35)

        btn_signup = tk.Button(login_frame, command=self.open_signup, text="Signup", font=("times new roman", 15), activebackground="#EC4D37", fg="red", activeforeground="#1D1B1B", cursor="hand2")
        btn_signup.place(x=200, y=300, width=100, height=35)

    def login(self):
        username = self.email.get()
        password = self.password.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                con = sqlite3.connect("registration.db")
                cur = con.cursor()

                cur.execute("SELECT category FROM user_accounts WHERE username=? AND password=?", (username, password))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
                    self.password.set("")
                else:
                    category = row[0]
                    con.close()

                    if category == "HR":
                        self.root.destroy()
                        self.hr()
                    elif category == "Accounts":
                        self.root.destroy()
                        self.accounts()
                    elif category == "User":
                        self.root.destroy()
                        self.display_user_content()
                    else:
                        messagebox.showerror("Error", "Invalid category", parent=self.root)

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def open_signup(self):
       # Register()
        self.root.destroy()
        import signup


    def hr(self):
        hrboardForm()

    def accounts(self):
        accboardForm()

    def display_user_content(self):
        
        pass

root = tk.Tk()
obj = Login_System(root)
root.mainloop()