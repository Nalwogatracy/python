import tkinter as tk
from tkinter import Image, ttk
# from PIL import Image, ImageTk
import sqlite3
from datetime import datetime
from hr_table import EmployeeTable

class EmployeeForm(tk.Tk):
    def open_employee_table(self):
        employee_table = EmployeeTable()

    def rearrange_start_date_format(self, event):
        start_date_str = self.start_date_entry.get()
        if start_date_str:
            try:
                start_date_datetime = datetime.strptime(start_date_str, "%Y-%m-%d")
                start_date_formatted = start_date_datetime.strftime("%d-%m-%Y")
                self.start_date_entry.delete(0, tk.END)
                self.start_date_entry.insert(0, start_date_formatted)
            except ValueError:
                print("Invalid date format. Please use the format YYYY-MM-DD.")

    def calculate_age(self):
        dob_str = self.dob_entry.get()
        if dob_str:
            try:
                dob_datetime = datetime.strptime(dob_str, "%Y-%m-%d")
                age = datetime.now().year - dob_datetime.year - ((datetime.now().month, datetime.now().day) < (dob_datetime.month, dob_datetime.day))
                self.age_entry.config(state='normal')
                self.age_entry.delete(0, tk.END)
                self.age_entry.insert(0, age)
                self.age_entry.config(state='readonly')
            except ValueError:
                print("Invalid date format. Please use the format YYYY-MM-DD.")

    def __init__(self):
        super().__init__()

        self.title("Pay Roll Systen/Add Employee")
        self.geometry("1366x768+0+0")

        self.header_frame = tk.Frame(self,relief=tk.RIDGE,bg="white")
        self.header_frame.place(x=0,y=0,width=1320,height=80)

        progressbar = ttk.Progressbar(self.header_frame, orient="horizontal", length=1520, mode="determinate", value=100)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("color.Horizontal.TProgressbar", foreground="blue", background="blue")
        progressbar.config(style="color.Horizontal.TProgressbar")
        progressbar.place(x=220, y=50)

        self.heading_label = tk.Label(self.header_frame, bg="white", fg="blue", text="Employee PayRoll System >>  Add Employee", font=("Times New Roman", 16, "bold"))
        self.heading_label.place(x=220, y=5)

        self.sidebar = tk.Frame(self, width=200, bg="blue")
        self.sidebar.pack(side="left", fill="y")

        self.link_frame = tk.Frame(self.sidebar, relief=tk.RIDGE,bg="blue")
        self.link_frame.place(x=25,y=150,width=150,height=300)

        self.home_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Home", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w")
        self.home_button.pack(pady=10)
        self.home_button.config(cursor="hand2")

        self.workers_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Add Employee", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w" )
        self.workers_button.pack(pady=10)
        self.workers_button.config(cursor="hand2")

        self.view_employee_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="View Employees", width=20, background="blue", font=("Times New Roman",  12, "bold") , anchor="w", command=self.open_employee_table)
        self.view_employee_button.pack(pady=10)
        self.view_employee_button.config(cursor="hand2")

        self.delete_edit_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Delete", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w")
        self.delete_edit_button.pack(pady=10)
        self.delete_edit_button.config(cursor="hand2")

        self.create_user_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="User Account", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w", command=self.signup)
        self.create_user_button.pack(pady=10)
        self.create_user_button.config(cursor="hand2")

        self.logout_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Log-Out", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w")
        self.logout_button.pack(pady=10)
        self.logout_button.config(cursor="hand2")


        self.details_frame = tk.Frame(self, relief=tk.RIDGE,bg="white")
        self.details_frame.place(x=220,y=70,width=400,height=360)


        self.employee_id_label = tk.Label(self.details_frame, text="Employee ID:", font=("Times New Roman", 13), bg="white", anchor="w")
        self.employee_id_entry = tk.Entry(self.details_frame, font=("Times New Roman", 13))

        self.name_label = tk.Label(self.details_frame, text="Name:", font=("Times New Roman", 13), bg="white", anchor="w")
        self.name_entry = tk.Entry(self.details_frame, font=("Times New Roman", 13))

        self.residence_label = tk.Label(self.details_frame, text="Residence:", font=("Times New Roman", 13), bg="white", anchor="w")
        self.residence_entry = tk.Entry(self.details_frame, font=("Times New Roman", 13))

        self.origin_label = tk.Label(self.details_frame, text="Origin:", font=("Times New Roman", 13), bg="white", anchor="w")
        self.origin_entry = tk.Entry(self.details_frame, font=("Times New Roman", 13))

        self.email_label = tk.Label(self.details_frame, text="Email:", font=("Times New Roman", 13), bg="white", anchor="w")
        self.email_entry = tk.Entry(self.details_frame, font=("Times New Roman", 13))

        self.dob_label = tk.Label(self.details_frame, text="DOB(yyy-mm-dd):", font=("Times New Roman", 13), bg="white", anchor="w")
        self.dob_entry = tk.Entry(self.details_frame, font=("Times New Roman", 13))
        self.dob_entry.bind("<FocusOut>", self.rearrange_dob_format)
        self.dob_entry.bind("<FocusOut>", lambda event: self.calculate_age())

        self.age_label = tk.Label(self.details_frame, text="Age:", font=("Times New Roman", 13), bg="white", anchor="w")
        self.age_entry = tk.Entry(self.details_frame, state='readonly', font=("Times New Roman", 13))

        self.gender_label = tk.Label(self.details_frame, text="Gender:", font=("Times New Roman", 13), bg="white", anchor="w")
        self.gender_combobox = ttk.Combobox(self.details_frame, values=["Male", "Female"], font=("Times New Roman", 13))

        self.contact_label = tk.Label(self.details_frame, text="Contact:", font=("Times New Roman", 13), bg="white", anchor="w")
        self.contact_entry = tk.Entry(self.details_frame, font=("Times New Roman", 13))

        self.start_date_label = tk.Label(self.details_frame, text="Start Date(yyy-mm-dd):", font=("Times New Roman", 13), bg="white", anchor="w")
        self.start_date_entry = tk.Entry(self.details_frame, font=("Times New Roman", 13))
        self.start_date_entry.bind("<FocusOut>", self.rearrange_start_date_format)


        self.responsibilities_frame = tk.Frame(self, relief=tk.RIDGE,bg="white")
        self.responsibilities_frame.place(x=800,y=70,width=350,height=360)


        # Responsibility Labels and Checkboxes
        self.responsibilities_label = tk.Label(self.responsibilities_frame, text="Responsibilities:", bg="white", anchor="w", font=("Times New Roman", 13))
      
        self.admin_vc_var = tk.IntVar()
        self.admin_vc_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Admin-VC", variable=self.admin_vc_var, bg="white", anchor="w", font=("Times New Roman", 13))

        self.admin_dvc_var = tk.IntVar()
        self.admin_dvc_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Admin-DVC", variable=self.admin_dvc_var, bg="white", anchor="w", font=("Times New Roman", 13))

        self.admin_registrar_var = tk.IntVar()
        self.admin_registrar_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Admin-Registrar", variable=self.admin_registrar_var, bg="white", anchor="w", font=("Times New Roman", 13))

        self.admin_ass_registra_var = tk.IntVar()
        self.admin_ass_registra_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Admin-AssRegistra", variable=self.admin_ass_registra_var, bg="white", anchor="w", font=("Times New Roman", 13))

        self.admin_hr_var = tk.IntVar()
        self.admin_hr_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Admin-HR", variable=self.admin_hr_var, bg="white", anchor="w", font=("Times New Roman", 13))

        self.admin_dean_var = tk.IntVar()
        self.admin_dean_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Admin-Dean", variable=self.admin_dean_var, bg="white", anchor="w", font=("Times New Roman", 13))

        self.admin_other_var = tk.IntVar()
        self.admin_other_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Admin-Other", variable=self.admin_other_var, bg="white", anchor="w", font=("Times New Roman", 13))

        self.dean_var = tk.IntVar()
        self.dean_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Dean", variable=self.dean_var, bg="white", anchor="w", font=("Times New Roman", 13))

        self.hod_var = tk.IntVar()
        self.hod_checkbox = tk.Checkbutton(self.responsibilities_frame, text="HOD", variable=self.hod_var, bg="white", anchor="w", font=("Times New Roman", 13))

        self.lecturer_var = tk.IntVar()
        self.lecturer_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Lecturer", variable=self.lecturer_var, bg="white", anchor="w", font=("Times New Roman", 13))

        self.secretary_var = tk.IntVar()
        self.secretary_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Secretary", variable=self.secretary_var, bg="white", anchor="w", font=("Times New Roman", 13))

        self.security_var = tk.IntVar()
        self.security_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Security", variable=self.security_var, bg="white", anchor="w", font=("Times New Roman", 13))


        self.cleaner_var = tk.IntVar()
        self.cleaner_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Cleaner", variable=self.cleaner_var, bg="white", anchor="w", font=("Times New Roman", 13))

        self.student_labor_var = tk.IntVar()
        self.student_labor_checkbox = tk.Checkbutton(self.responsibilities_frame, text="Student-Labour", variable=self.student_labor_var, bg="white", anchor="w", font=("Times New Roman", 13))

      
        self.employee_id_label.grid(row=0, column=0, sticky="w")
        self.employee_id_entry.grid(row=0, column=1, pady=5)
        self.name_label.grid(row=1, column=0, sticky="w")
        self.name_entry.grid(row=1, column=1, pady=5)
        self.residence_label.grid(row=2, column=0, sticky="w")
        self.residence_entry.grid(row=2, column=1, pady=5)
        self.origin_label.grid(row=3, column=0, sticky="w")
        self.origin_entry.grid(row=3, column=1, pady=5)
        self.email_label.grid(row=4, column=0, sticky="w")
        self.email_entry.grid(row=4, column=1, pady=5)
        self.dob_label.grid(row=5, column=0, sticky="w")
        self.dob_entry.grid(row=5, column=1, pady=5)
        self.age_label.grid(row=6, column=0, sticky="w")
        self.age_entry.grid(row=6, column=1, pady=5)
        self.gender_label.grid(row=7, column=0, sticky="w")
        self.gender_combobox.grid(row=7, column=1, pady=5)
        self.contact_label.grid(row=8, column=0, sticky="w")
        self.contact_entry.grid(row=8, column=1, pady=5)
        self.start_date_label.grid(row=9, column=0, sticky="w")
        self.start_date_entry.grid(row=9, column=1, pady=5)

  
        self.responsibilities_label.grid(row=0, column=0, sticky="e")
        self.admin_vc_checkbox.grid(row=0, column=1, sticky="w")
        self.admin_dvc_checkbox.grid(row=1, column=1, sticky="w")
        self.admin_registrar_checkbox.grid(row=2, column=1, sticky="w")
        self.admin_ass_registra_checkbox.grid(row=3, column=1, sticky="w")
        self.admin_hr_checkbox.grid(row=4, column=1, sticky="w")
        self.admin_dean_checkbox.grid(row=5, column=1, sticky="w")
        self.admin_other_checkbox.grid(row=6, column=1, sticky="w")
        self.dean_checkbox.grid(row=7, column=1, sticky="w")
        self.hod_checkbox.grid(row=8, column=1, sticky="w")
        self.lecturer_checkbox.grid(row=9, column=1, sticky="w")
        self.secretary_checkbox.grid(row=10, column=1, sticky="w")
        self.security_checkbox.grid(row=11, column=1, sticky="w")
        self.cleaner_checkbox.grid(row=12, column=1, sticky="w")
        self.student_labor_checkbox.grid(row=13, column=1, sticky="w")

        self.button_frame = tk.Frame(self, relief=tk.RIDGE,bg="white")
        self.button_frame.place(x=350,y=500,width=500,height=50)

        self.connection = sqlite3.connect("registration.db")
        self.cursor = self.connection.cursor()
        self.create_table()
        #self.delete_button = tk.Button(self, text="Delete", command=self.delete_row)
        #self.delete_button.pack(pady=10)

        # image_path = "images/images.png"  
        # image = Image.open(image_path)
        # photo = ImageTk.PhotoImage(image, width=50)
        # image = image.resize((10, 10))
        # label = tk.Label(self.responsibilities_frame, image=photo)
        # label.image = photo
        # label.place(x=0, y=1)
        # Place other elements inside the card frame

        self.logo = tk.Canvas(self, width=60, height=60, highlightthickness=0, bg="white")  # Canvas for circular frame
        self.logo.place(x=30, y=4)

        # Load and resize logo image
        # logo_image = Image.open("images/images.png")
        # logo_image = logo_image.resize((50, 50))  # Adjust size if needed
        # self.logo_photo = ImageTk.PhotoImage(logo_image)

        # # Create a circle inside the canvas (circular frame)
        # center_x = 30  # Adjust based on logo frame placement (x + width/2)
        # center_y = 22  # Adjust based on logo frame placement (y + height/2)
        # radius = 25  # Adjust radius for desired circle size
        # self.logo.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill="white")

        # # Display the logo image on the canvas
        # self.logo.create_image(center_x, center_y, anchor="center", image=self.logo_photo)
        
        # # Create a label to display the logo image
        # self.logo_label = tk.Label(self.logo, image=self.logo_photo)
        # self.logo_label.pack()s

        self.foot_frame = tk.Frame(self,relief=tk.RIDGE,bg="white")
        self.foot_frame.place(x=230,y=450,width=1100,height=100)

        progressbar = ttk.Progressbar(self.foot_frame, orient="horizontal", length=1100, mode="determinate", value=100)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("color.Horizontal.TProgressbar", foreground="royal blue", background="royal blue")
        progressbar.config(style="color.Horizontal.TProgressbar")
        progressbar.place(x=0, y=70)

        self.add_button = tk.Button(self.foot_frame, text="Add Employee", command=self.add_employee, bg="royal blue", fg="white", font=("times new roman", 12))
        self.add_button.place(x=500,y=0,width=150,height=50)


        self.footer_frame = tk.Frame(self,relief=tk.RIDGE,bg="royal blue")
        self.footer_frame.place(x=230,y=550,width=1100,height=200)
        self.heading_label = tk.Label(self.footer_frame, bg="royal blue", fg="white", text="@2024 All rights reserved - Bugema University", font=("Times New Roman", 10, "bold"))
        self.heading_label.place(x=400, y=100)
    
    def signup(self):
        #self.app.destroy()
        import signup

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                                employee_id TEXT PRIMARY KEY,
                                name TEXT,
                                residence TEXT,
                                origin TEXT,
                                email TEXT,
                                dob TEXT,
                                age INTEGER,
                                gender TEXT,
                                contact TEXT,
                                start_date TEXT,
                                responsibilities TEXT
                                )''')
        self.connection.commit()

    def add_employee(self):
        # Get values from entry boxes
        employee_id = self.employee_id_entry.get()
        name = self.name_entry.get()
        residence = self.residence_entry.get()
        origin = self.origin_entry.get()
        email = self.email_entry.get()
        dob = self.dob_entry.get()
        age = self.age_entry.get()
        gender = self.gender_combobox.get()
        contact = self.contact_entry.get()
        start_date = self.start_date_entry.get()
        responsibilities = self.get_responsibilities()

        # Insert values into database
        self.cursor.execute('''INSERT INTO employees (employee_id, name, residence, origin, email, dob, age, gender, contact, start_date, responsibilities)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (employee_id, name, residence, origin, email, dob, age, gender, contact, start_date, responsibilities))
        self.connection.commit()
        print("Employee added successfully.")

    def get_responsibilities(self):
        responsibilities = []
        checkboxes = [
            (self.admin_vc_var, "Admin-VC"),
            (self.admin_dvc_var, "Admin-DVC"),
            (self.admin_registrar_var, "Admin-Registrar"),
            (self.admin_ass_registra_var, "Admin-AssRegistra"),
            (self.admin_hr_var, "Admin-HR"),
            (self.admin_dean_var, "Admin-Dean"),
            (self.admin_other_var, "Admin-Other"),
            (self.dean_var, "Dean"),
            (self.hod_var, "HOD"),
            (self.lecturer_var, "Lecturer"),
            (self.secretary_var, "Secretary"),
            (self.cleaner_var, "Cleaner"),
            (self.student_labor_var, "Student-Labour")
        ]
        for checkbox_var, text in checkboxes:
            if checkbox_var.get() == 1:
                responsibilities.append(text)
        return ", ".join(responsibilities)

    def rearrange_dob_format(self, event):
        dob_str = self.dob_entry.get()
        if dob_str:
            try:
                dob_datetime = datetime.strptime(dob_str, "%Y-%m-%d")
                dob_formatted = dob_datetime.strftime("%d-%m-%Y")
                self.dob_entry.delete(0, tk.END)
                self.dob_entry.insert(0, dob_formatted)
                self.calculate_age()  
            except ValueError:
                print("Invalid date format. Please use the format YYYY-MM-DD.")

    
    def delete_row(self):
        employee_id = self.employee_id_entry.get()
        if employee_id:
            connection = sqlite3.connect("registration.db")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM employees WHERE employee_id = ?", (employee_id,))
            cursor.execute("DELETE FROM account WHERE employee_id = ?", (employee_id,))
            connection.commit()
            connection.close()


if __name__ == "__main__":
    appp = EmployeeForm()
    appp.config(bg="white")
    appp.mainloop()
