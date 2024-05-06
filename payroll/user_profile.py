import tkinter as tk
from tkinter import messagebox,ttk
from hr_table import EmployeeTable
import sqlite3
from hr_table import EmployeeTable

window = tk.Tk()
window.title("Payroll System/Profile")
window.geometry("1366x768+0+0")
window.config(bg="white")
title = tk.Label(window, text="Employee Payroll management System",font=("Arial",30,"bold") ,bg="black" ,fg="yellow" ,anchor="center",padx=10).place(x=0,y=0,relwidth=1)


#This is frame 1
frame1 = tk.Frame(window,bd=3,relief="sunken",bg="blue")
frame1.place(x=0,y=50,width=250,height=642)

title2 = tk.Label(frame1, text="User Profile",font=("Arial",20),bg="white"  ,fg="black" ,anchor="center" ,padx=10).place(x=0,y=0,relwidth=1)

label_Home = tk.Label(frame1, text="Home",font=("Arial",15) ,bg="blue",fg="white",anchor="center" ).place(x=50,y=90)

label_View = tk.Label(frame1, text="View Details",font=("Times New Roman",15) ,fg="white",bg="blue",anchor="center" ).place(x=50,y=160)


label_Check_account = tk.Label(frame1, text="Acount",font=("Times New Roman",15) ,fg="white",bg="blue" ,anchor="center").place(x=50,y=230)

label_Help = tk.Label(frame1, text="Help",font=("Times New Roman",15) ,fg="white",bg="blue",anchor="center" ).place(x=50,y=320)

btn_Logout = tk.Button(frame1, text="Logout",font=("Times New Roman",15) ,fg="white",bg="blue",anchor="center" ).place(x=50,y=420)


#This is my second frame
frame2 = tk.Frame(window,bd=3,relief="ridge",bg="white")
frame2.place(x=250,y=50,width=1150,height=642)

#This is my separator frame
frame3 = tk.Frame(window,bd=3,relief="sunken",bg="blue")
frame3.place(x=250,y=350,width=1150,height=10)

def fetch_data():
    conn = sqlite3.connect("registration.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

def populate_treeview(tree, data):
    
    for item in tree.get_children():
        tree.delete(item)
    for record in data:
        tree.insert("", "end", values=record)
data = fetch_data()
tree = ttk.Treeview(frame2, columns=("ID", "Name", "Age", "Department"), show="headings")
tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Department", text="Department")

tree.insert("", "end", text="1", values=("John Doe", 30, "USA"))
tree.insert("", "end", text="2", values=("Jane Smith", 25, "Canada"))
tree.insert("", "end", text="3", values=("Michael Johnson", 40, "UK"))
tree.pack(fill="both", expand=True)
populate_treeview(tree, data)







window.mainloop()