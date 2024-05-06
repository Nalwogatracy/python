import tkinter as tk
from tkinter import Image, ttk
#from PIL import Image, ImageTk
import sqlite3
from datetime import datetime
from hr_table import EmployeeTable
from hr_add import EmployeeForm
from hr_delete import hrdelForm
from account_add import addAccountForm
# from login import Login_System
from account_view import accViewForm
# from login import Login_System

class accboardForm(tk.Tk):
    def open_employee_table(self):
        app.destroy()
        accViewForm()

    
    def logout():
        app.destroy()
        
        
        
    
    def signup(self):
        import signup
    
    def add_employee(self):
        app.destroy()
        addAccountForm()
    
    def delete(self):
        app.destroy()
        hrdelForm()
    
    def logout(self):
        app.destroy()
        # Login_System()

    def __init__(self):
        super().__init__()

        self.title("Pay Roll Systen/Dashboard")
        self.geometry("1366x768+0+0")
        self.config(bg="black")

        self.overlay_frame = tk.Frame(self, bg="white")
        self.overlay_frame.pack(side="right", fill="both", expand=True)
        self.overlay_frame.place(x=0, y=0, width=1366, height=768)
        self.label = tk.Label(self.overlay_frame, text="DASHBOARD", font=("Arial", 14, "bold"), fg="white", bg="lightblue")
        self.label.place(relx=0.5, rely=0.5, anchor="center")


        self.header_frame = tk.Frame(self,relief=tk.RIDGE,bg="white")
        self.header_frame.place(x=230,y=0,width=1100,height=150)

        # self.heading_label = tk.Label(self.header_frame, bg="white", fg="royal blue", text="Employee PayRoll System >>  Add Employee", font=("Times New Roman", 16, "bold"))
        # self.heading_label.place(x=300, y=5)

        self.sidebar = tk.Frame(self, width=200, bg="blue")
        self.sidebar.pack(side="left", fill="y")

        self.link_frame = tk.Frame(self.sidebar, relief=tk.RIDGE,bg="blue")
        self.link_frame.place(x=20,y=70,width=150,height=300)
        
        self.home_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Home", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w")
        self.home_button.pack(pady=10)
        self.home_button.config(cursor="hand2")

        self.workers_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Add Employee", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w", command=self.add_employee)
        self.workers_button.pack(pady=10)
        self.workers_button.config(cursor="hand2")

        self.view_employee_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="View Employees", width=20, background="blue", font=("Times New Roman",  12, "bold") , anchor="w", command=self.open_employee_table)
        self.view_employee_button.pack(pady=10)
        self.view_employee_button.config(cursor="hand2")

        # self.delete_edit_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Employee Account", width=20, background="royal blue", font=("Times New Roman",  12, "bold"), anchor="w", command=self.delete)
        # self.delete_edit_button.pack(pady=10)
        # self.delete_edit_button.config(cursor="hand2")

        self.logo_frame = tk.Frame(self.sidebar, relief=tk.RIDGE,bg="white")
        self.logo_frame.place(x=25,y=50)
        self.logo = tk.Label(self.logo_frame, borderwidth=0, foreground="black", text="ACCOUNTS", width=94, background="blue", font=("Times New Roman",  12, "bold"), anchor="w")
        self.logo.pack()

        self.create_user_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="User Account", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w", command=self.signup)
        self.create_user_button.pack(pady=10)
        self.create_user_button.config(cursor="hand2")

        self.logout_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Log-Out", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w", command=self.logout)
        self.logout_button.pack(pady=10)
        self.logout_button.config(cursor="hand2")

        # self.create_landing_page()



    # def create_landing_page(self):
        self.landing_page_frame = tk.Frame(self, bg="white")
        self.landing_page_frame.place(y=130, x=350, width=900, height=400)

        progressbar = ttk.Progressbar(self.header_frame, orient="horizontal", length=1120, mode="determinate", value=100)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("color.Horizontal.TProgressbar", foreground="royal blue", background="blue")
        progressbar.config(style="color.Horizontal.TProgressbar")
        progressbar.place(x=5, y=80)

        self.lab = tk.Label(self.header_frame, text="PAY-ROLL SYSTEM DASHBOARD", font=("Arial", 34, "bold"), fg="royal blue", bg="white")
        self.lab.place(x=170, y=20)

        self.square_frame_1 = tk.Frame(self.landing_page_frame, width=200, height=200, bg="Green")
        self.square_frame_1.place(x=0, y=0)
        self.square_frame_1.bind("<Enter>", lambda event: self.change_bg_color(self.square_frame_1, "Yellow"))
        self.square_frame_1.bind("<Leave>", lambda event: self.change_bg_color(self.square_frame_1, "Green"))

        self.label_1 = tk.Label(self.square_frame_1, text="View Employees", font=("Arial", 14, "bold"), fg="white", bg="lightgreen")
        self.label_1.place(relx=0.5, rely=0.5, anchor="center")

        self.button_1 = tk.Button(self.square_frame_1, text="View Employees >>", command=self.open_employee_table)
        self.button_1.place(relx=0.5, rely=0.7, anchor="center")

        self.square_frame_2 = tk.Frame(self.landing_page_frame, width=200, height=200, bg="lightblue")
        self.square_frame_2.place(x=340, y=0)
        self.square_frame_2.bind("<Enter>", lambda event: self.change_bg_color(self.square_frame_2, "red"))
        self.square_frame_2.bind("<Leave>", lambda event: self.change_bg_color(self.square_frame_2, "lightblue"))

        self.label_2 = tk.Label(self.square_frame_2, text="Add Employee", font=("Arial", 14, "bold"), fg="white", bg="lightblue")
        self.label_2.place(relx=0.5, rely=0.5, anchor="center")

        self.button_2 = tk.Button(self.square_frame_2, text="Add Employee >>", command=self.add_employee)
        self.button_2.place(relx=0.5, rely=0.7, anchor="center")

        self.square_frame_3 = tk.Frame(self.landing_page_frame, width=200, height=200, bg="pink")
        self.square_frame_3.place(x=650, y=0)
        self.square_frame_3.bind("<Enter>", lambda event: self.change_bg_color(self.square_frame_3, "purple"))
        self.square_frame_3.bind("<Leave>", lambda event: self.change_bg_color(self.square_frame_3, "pink"))

        self.label_3 = tk.Label(self.square_frame_3, text="Create Account", font=("Arial", 14, "bold"), fg="white", bg="pink")
        self.label_3.place(relx=0.5, rely=0.5, anchor="center")

        self.button_3 = tk.Button(self.square_frame_3, text="Create Account >>", command=self.signup)
        self.button_3.place(relx=0.5, rely=0.7, anchor="center")

        self.button_1.bind("<Enter>", lambda event: self.change_button_style(self.button_1, "pink"))
        self.button_1.bind("<Leave>", lambda event: self.change_button_style(self.button_1, "lightgreen"))

        self.button_2.bind("<Enter>", lambda event: self.change_button_style(self.button_2, "red"))
        self.button_2.bind("<Leave>", lambda event: self.change_button_style(self.button_2, "lightblue"))

        self.button_3.bind("<Enter>", lambda event: self.change_button_style(self.button_3, "purple"))
        self.button_3.bind("<Leave>", lambda event: self.change_button_style(self.button_3, "pink"))

        self.footer_frame = tk.Frame(self,relief=tk.RIDGE,bg="blue")
        self.footer_frame.place(x=230,y=550,width=1100,height=200)
        self.heading_label = tk.Label(self.footer_frame, bg="blue", fg="white", text="@2024 All rights reserved - Bugema University", font=("Times New Roman", 10, "bold"))
        self.heading_label.place(x=400, y=100)
    

    def change_button_style(self, button, color):
        button.config(bg=color)

    def change_bg_color(self, frame, color):
        frame.config(bg=color)
    
    def signup(self):
        app.destroy()
        import signup
    


if __name__ == "__main__":
    app = accboardForm()
    app.config(bg="white")
    app.mainloop()
