import tkinter as tk
from tkinter import ttk
import sqlite3

class addAccountForm(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title("Pay-Roll system/Accounts Add")
        self.geometry("1366x768+0+0")

        self.header_frame = tk.Frame(self,relief=tk.RIDGE,bg="white")
        self.header_frame.place(x=0,y=0,width=1320,height=80)

        progressbar = ttk.Progressbar(self.header_frame, orient="horizontal", length=1520, mode="determinate", value=100)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("color.Horizontal.TProgressbar", foreground="royal blue", background="blue")
        progressbar.config(style="color.Horizontal.TProgressbar")
        progressbar.place(x=220, y=50)

        self.heading_label = tk.Label(self.header_frame, bg="white", fg="blue", text="Employee PayRoll System >>  Add New Employee", font=("Times New Roman", 16, "bold"))
        self.heading_label.place(x=220, y=5)

        self.sidebar = tk.Frame(self, width=200, bg="blue")
        self.sidebar.pack(side="left", fill="y")


        self.link_frame = tk.Frame(self.sidebar, relief=tk.RIDGE,bg="blue")
        self.link_frame.place(x=25,y=150,width=150,height=300)

        self.home_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Home", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w")
        self.home_button.pack(pady=20)
        self.home_button.config(cursor="hand2")

        self.workers_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Add Employee", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w" )
        self.workers_button.pack(pady=20)
        self.workers_button.config(cursor="hand2")

        # self.view_employee_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="View Employees", width=20, background="royal blue", font=("Times New Roman",  12, "bold") , anchor="w")
        # self.view_employee_button.pack(pady=10)
        # self.view_employee_button.config(cursor="hand2")

        self.delete_edit_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Delete", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w")
        self.delete_edit_button.pack(pady=10)
        self.delete_edit_button.config(cursor="hand2")

        self.create_user_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="User Account", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w")
        self.create_user_button.pack(pady=20)
        self.create_user_button.config(cursor="hand2")

        self.logout_button = tk.Button(self.link_frame, borderwidth=0, foreground="white", text="Log-Out", width=20, background="blue", font=("Times New Roman",  12, "bold"), anchor="w")
        self.logout_button.pack(pady=10)
        self.logout_button.config(cursor="hand2")


        self.account_frame = tk.Frame(self, relief=tk.RIDGE, bg="white")
        self.account_frame.place(x=230,y=100,width=450,height=200)


        self.name_label = tk.Label(self.account_frame, text="Name:", font=("Times New Roman", 13), bg="white")
        self.name_label.grid(row=0, column=0, sticky="w", pady=10)
        

        self.name_combobox = ttk.Combobox(self.account_frame, state="readonly", postcommand=self.fetch_employee_details)
        self.name_combobox.grid(row=0, column=1, pady=10)
        
        self.employee_id_label = tk.Label(self.account_frame, text="Employee ID:", font=("Times New Roman", 13), bg="white")
        self.employee_id_label.grid(row=1, column=0, sticky="w", pady=10)
        self.employee_id_entry = tk.Entry(self.account_frame, state='readonly')
        self.employee_id_entry.grid(row=1, column=1, pady=10)

        self.responsibility_label = tk.Label(self.account_frame, text="Responsibility:", font=("Times New Roman", 13), bg="white")
        self.responsibility_label.grid(row=2, column=0, sticky="w", pady=10)
        self.responsibility_entry = tk.Entry(self.account_frame, state='readonly')
        self.responsibility_entry.grid(row=2, column=1, pady=10)

        self.allowances_label = tk.Label(self.account_frame, text="Allowances:", font=("Times New Roman", 13), bg="white", fg="black")
        self.allowances_label.grid(row=5, column=0, sticky="w", pady=10)
        self.allowances_entry = tk.Entry(self.account_frame)
        self.allowances_entry.grid(row=5, column=1, pady=10)

        self.save_button = tk.Button(self, text="Save", command=self.save_account)
        self.save_button.pack(pady=10)



        self.name_combobox.bind("<<ComboboxSelected>>", self.fetch_employee_id)

 
        self.create_account_table()

        self.taxes_frame = tk.Frame(self, relief=tk.RIDGE, bg="white")
        self.taxes_frame.place(x=230,y=320,width=450,height=250)

        self.name_label = tk.Label(self.taxes_frame, text="Deductions", font=("Times New Roman", 16), bg="white", fg="royal blue")
        self.name_label.grid(row=0, column=0, sticky="w", pady=10)

        self.nssf_label = tk.Label(self.taxes_frame, text="NSSF", font=("Times New Roman", 13), bg="white", fg="black")
        self.nssf_label.grid(row=1, column=0, sticky="w", pady=10)
        self.nssf_tax = tk.Label(self.taxes_frame, text="10% of Basic Salary", font=("Times New Roman", 13), bg="white", fg="black")
        self.nssf_tax.grid(row=1, column=2, sticky="w", pady=10)

        self.paye_label = tk.Label(self.taxes_frame, text="PAYE", font=("Times New Roman", 13), bg="white", fg="black")
        self.paye_label.grid(row=2, column=0, sticky="w", pady=10)
        self.paye_tax = tk.Label(self.taxes_frame, text="5% of Basic Salary", font=("Times New Roman", 13), bg="white", fg="black")
        self.paye_tax.grid(row=2, column=2, sticky="w", pady=10)

        self.insurance_label = tk.Label(self.taxes_frame, text="Insurance", font=("Times New Roman", 13), bg="white", fg="black")
        self.insurance_label.grid(row=3, column=0, sticky="w", pady=10)
        self.insurance_tax = tk.Label(self.taxes_frame, text="5% of Basic Salary", font=("Times New Roman", 13), bg="white", fg="black")
        self.insurance_tax.grid(row=3, column=2, sticky="w", pady=10)

        self.tithe_label = tk.Label(self.taxes_frame, text="Tithe", font=("Times New Roman", 13), bg="white", fg="black")
        self.tithe_label.grid(row=4, column=0, sticky="w", pady=10)
        self.tithe_tax = tk.Label(self.taxes_frame, text="10% of Basic Salary", font=("Times New Roman", 13), bg="white", fg="black")
        self.tithe_tax.grid(row=4, column=2, sticky="w", pady=10)


        self.basic_frame = tk.Frame(self, bd=1, relief=tk.RIDGE, bg="white")
        self.basic_frame.place(x=500,y=80,width=350,height=500)

        self.name_label = tk.Label(self.basic_frame, text="Salary Structure", font=("Times New Roman", 16), bg="white", fg="royal blue")
        self.name_label.grid(row=0, column=0, sticky="w", pady=10)

        self.nssf_label = tk.Label(self.basic_frame, text="Vice Chancellor", font=("Times New Roman", 13), bg="white", fg="black")
        self.nssf_label.grid(row=1, column=0, sticky="w", pady=5)
        self.nssf_tax = tk.Label(self.basic_frame, text="UGx.5,000,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.nssf_tax.grid(row=1, column=2, sticky="w", pady=5)

        self.paye_label = tk.Label(self.basic_frame, text="Deputy VC", font=("Times New Roman", 13), bg="white", fg="black")
        self.paye_label.grid(row=2, column=0, sticky="w", pady=5)
        self.paye_tax = tk.Label(self.basic_frame, text="UGx.4,000,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.paye_tax.grid(row=2, column=2, sticky="w", pady=5)

        self.insurance_label = tk.Label(self.basic_frame, text="Registrar", font=("Times New Roman", 13), bg="white", fg="black")
        self.insurance_label.grid(row=3, column=0, sticky="w", pady=5)
        self.insurance_tax = tk.Label(self.basic_frame, text="UGx.3,000,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.insurance_tax.grid(row=3, column=2, sticky="w", pady=5)

        self.tithe_label = tk.Label(self.basic_frame, text="Ass. Registrar", font=("Times New Roman", 13), bg="white", fg="black")
        self.tithe_label.grid(row=4, column=0, sticky="w", pady=5)
        self.tithe_tax = tk.Label(self.basic_frame, text="UGx.2,500,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.tithe_tax.grid(row=4, column=2, sticky="w", pady=5)

        self.hr_label = tk.Label(self.basic_frame, text="Human Resource", font=("Times New Roman", 13), bg="white", fg="black")
        self.hr_label.grid(row=5, column=0, sticky="w", pady=5)
        self.hr = tk.Label(self.basic_frame, text="UGx.2,000,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.hr.grid(row=5, column=2, sticky="w", pady=5)

        self.dean_label = tk.Label(self.basic_frame, text="Dean of Students", font=("Times New Roman", 13), bg="white", fg="black")
        self.dean_label.grid(row=6, column=0, sticky="w", pady=5)
        self.dean = tk.Label(self.basic_frame, text="UGx.1,600,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.dean.grid(row=6, column=2, sticky="w", pady=5)

        self.admin_label = tk.Label(self.basic_frame, text="Other Admin", font=("Times New Roman", 13), bg="white", fg="black")
        self.admin_label.grid(row=7, column=0, sticky="w", pady=5)
        self.admin = tk.Label(self.basic_frame, text="UGx.1,000,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.admin.grid(row=7, column=2, sticky="w", pady=5)

        self.sch_label = tk.Label(self.basic_frame, text="Dean of School", font=("Times New Roman", 13), bg="white", fg="black")
        self.sch_label.grid(row=8, column=0, sticky="w", pady=5)
        self.sch = tk.Label(self.basic_frame, text="UGx.800,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.sch.grid(row=8, column=2, sticky="w", pady=5)

        self.hod_label = tk.Label(self.basic_frame, text="Head of Department", font=("Times New Roman", 13), bg="white", fg="black")
        self.hod_label.grid(row=9, column=0, sticky="w", pady=5)
        self.hod = tk.Label(self.basic_frame, text="UGx.500,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.hod.grid(row=9, column=2, sticky="w", pady=5)

        self.lec_label = tk.Label(self.basic_frame, text="Lecturer", font=("Times New Roman", 13), bg="white", fg="black")
        self.lec_label.grid(row=10, column=0, sticky="w", pady=5)
        self.lec = tk.Label(self.basic_frame, text="UGx.1,000,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.lec.grid(row=10, column=2, sticky="w", pady=5)

        self.sec_label = tk.Label(self.basic_frame, text="Secretary", font=("Times New Roman", 13), bg="white", fg="black")
        self.sec_label.grid(row=11, column=0, sticky="w", pady=5)
        self.sec = tk.Label(self.basic_frame, text="UGx.500,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.sec.grid(row=11, column=2, sticky="w", pady=5)

        self.cle_label = tk.Label(self.basic_frame, text="Cleaner", font=("Times New Roman", 13), bg="white", fg="black")
        self.cle_label.grid(row=12, column=0, sticky="w", pady=5)
        self.cle = tk.Label(self.basic_frame, text="UGx.200,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.cle.grid(row=12, column=2, sticky="w", pady=5)

        self.stu_label = tk.Label(self.basic_frame, text="Student Labour", font=("Times New Roman", 13), bg="white", fg="black")
        self.stu_label.grid(row=13, column=0, sticky="w", pady=5)
        self.stu = tk.Label(self.basic_frame, text="UGx.100,000", font=("Times New Roman", 13), bg="white", fg="black")
        self.stu.grid(row=13, column=2, sticky="w", pady=5)



        self.allowances_frame = tk.Frame(self,  relief=tk.RIDGE, bg="white")
        self.allowances_frame.place(x=850, y=100, width=500, height=500)

        self.transport_var = tk.StringVar()
        self.housing_var = tk.StringVar()
        self.medical_var = tk.StringVar()
        self.research_var = tk.StringVar()
        self.communication_var = tk.StringVar()
        self.meals_var = tk.StringVar()
        self.clothing_var = tk.StringVar()
        self.special_duty_var = tk.StringVar()

        self.create_radiobutton("Transport", self.transport_var, 20, 5, {"Executive": 200000, "Admin": 100000, "Staff": 50000, "Other": 30000})
        self.create_radiobutton("Housing", self.housing_var, 20, 55, {"Executive": 500000, "Admin": 300000, "Staff": 200000, "Other": 10000})
        self.create_radiobutton("Medical", self.medical_var, 20, 105, {"Executive": 100000, "Admin": 50000, "Staff": 30000, "Other": 20000})
        self.create_radiobutton("Research", self.research_var, 20, 155, {"Executive": 100000, "Admin": 50000, "Staff": 30000, "Other": 10000})
        self.create_radiobutton("Communication", self.communication_var, 20, 205, {"Executive": 50000, "Admin": 30000, "Staff": 20000, "Other": 10000})
        self.create_radiobutton("Meals", self.meals_var, 20, 255, {"Executive": 450000, "Admin": 300000, "Staff": 200000, "Other": 10000})
        self.create_radiobutton("Clothing", self.clothing_var, 20, 305, {"Executive": 100000, "Admin": 50000, "Staff": 30000, "Other": 20000})
        self.create_radiobutton("Special Duty", self.special_duty_var, 20, 355, {"Executive": 50000, "Admin": 30000, "Staff": 20000, "Other": 10000})

        self.calculate_button = tk.Button(self.allowances_frame, text="Calculate", command=self.calculate_allowances, font=("Times New Roman", 13), bg="green", fg="white")
        self.calculate_button.place(x=200, y=400)


        self.foot_frame = tk.Frame(self,relief=tk.RIDGE,bg="white")
        self.foot_frame.place(x=230,y=600,width=1100,height=100)

        progressbar = ttk.Progressbar(self.foot_frame, orient="horizontal", length=1100, mode="determinate", value=100)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("color.Horizontal.TProgressbar", foreground="royal blue", background="royal blue")
        progressbar.config(style="color.Horizontal.TProgressbar")
        progressbar.place(x=0, y=70)

        self.add_button = tk.Button(self.foot_frame, text="Add Employee", command=self.save_account,  bg="royal blue", fg="white", font=("times new roman", 12))
        self.add_button.place(x=500,y=0,width=150,height=50)

    def create_radiobutton(self, text, var, x, y, rates):
        label = tk.Label(self.allowances_frame, text=text + ":", font=("Times New Roman", 12), bg="white", fg="blue")
        label.place(x=x, y=y)

        exec_btn = tk.Radiobutton(self.allowances_frame, text="Executive", font=("Times New Roman", 10), bg="white", fg="black", variable=var, value="Executive", command=self.update_color)
        exec_btn.place(x=x+100, y=y)

        admin_btn = tk.Radiobutton(self.allowances_frame, text="Admin", font=("Times New Roman", 10), bg="white", fg="black", variable=var, value="Admin", command=self.update_color)
        admin_btn.place(x=x+180, y=y)

        staff_btn = tk.Radiobutton(self.allowances_frame, text="Staff", font=("Times New Roman", 10), bg="white", fg="black", variable=var, value="Staff", command=self.update_color)
        staff_btn.place(x=x+260, y=y)

        other_btn = tk.Radiobutton(self.allowances_frame, text="Other", font=("Times New Roman", 10), bg="white", fg="black", variable=var, value="Other", command=self.update_color)
        other_btn.place(x=x+340, y=y)

        var.rates = rates

    def calculate_allowances(self):
        allowances_list = []
        total_allowances = 0
        checkboxes = [self.transport_var, self.housing_var, self.medical_var, self.research_var, self.communication_var, self.meals_var, self.clothing_var, self.special_duty_var]
    
        for checkbox in checkboxes:
            selected_option = checkbox.get()
            rates = checkbox.rates
            if selected_option in rates:
                allowance_value = rates[selected_option]
                allowances_list.append(f"{selected_option}-{allowance_value}")
                total_allowances += allowance_value

        allowances_text = ", ".join(allowances_list)
        result_label = tk.Label(self.allowances_frame, text=f"Total Allowances: {total_allowances}\n{allowances_text}", font=("Times New Roman", 12), bg="white", fg="blue", justify=tk.LEFT)
        result_label.place(x=20, y=430)
    def update_color(self):
        # Reset background color of all radio buttons
        self.reset_colors()
        selected_option = self.transport_var.get()
        # Change background color of the selected radio button
        if selected_option == "Executive":
            self.transport_executive.configure(bg="lightblue")
        elif selected_option == "Admin":
            self.transport_admin.configure(bg="lightblue")
        elif selected_option == "Staff":
            self.transport_staff.configure(bg="lightblue")
        elif selected_option == "Other":
            self.transport_other.configure(bg="lightblue")

    def reset_colors(self):
        # Reset background color of all radio buttons
        self.transport_executive.configure(bg="white")
        self.transport_admin.configure(bg="white")
        self.transport_staff.configure(bg="white")
        self.transport_other.configure(bg="white")
        # Reset background color for other allowances
        # Add similar lines for other allowances

    def create_account_table(self):
        connection = sqlite3.connect("registration.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS account (
                            employee_id TEXT PRIMARY KEY,
                            name TEXT,
                            responsibilities TEXT,
                            basic_salary REAL,
                            taxes REAL,
                            allowances REAL,
                            gross_pay REAL,
                            net_pay REAL
                        )''')
        connection.commit()
        connection.close()

    def fetch_employee_details(self):
        connection = sqlite3.connect("registration.db")
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM employees")
        employee_names = cursor.fetchall()
        if employee_names:
            self.name_combobox['values'] = [name[0] for name in employee_names]
        connection.close()

    def fetch_employee_id(self, event=None):
        connection = sqlite3.connect("registration.db")
        cursor = connection.cursor()
        # Fetch the employee ID and responsibility corresponding to the selected name
        selected_name = self.name_combobox.get()
        cursor.execute("SELECT employee_id, responsibilities FROM employees WHERE name=?", (selected_name,))
        employee_data = cursor.fetchone()
        if employee_data:
            # Auto-fill the employee ID entry
            self.employee_id_entry.config(state='normal')
            self.employee_id_entry.delete(0, tk.END)
            self.employee_id_entry.insert(0, employee_data[0])
            self.employee_id_entry.config(state='readonly')

            # Auto-fill the responsibility entry
            self.responsibility_entry.config(state='normal')
            self.responsibility_entry.delete(0, tk.END)
            self.responsibility_entry.insert(0, employee_data[1])
            self.responsibility_entry.config(state='readonly')
        connection.close()

    def calculate_basic_salary(self):
        responsibility = self.responsibility_entry.get()
        salary_mapping = {
            "Admin-VC": 5000000,
            "Admin-DVC": 4000000,
            "Admin-Registrar": 3000000,
            "Admin-AssRegistrar": 2500000,
            "Admin-HR": 2000000,
            "Admin-Dean": 1600000,
            "Admin-Other": 100000,
            "Dean": 800000,
            "HOD": 500000,
            "Lecturer": 1000000,
            "Secretary": 500000,
            "Cleaner": 200000,
            "Student-Labour": 100000
        }
        responsibilities = responsibility.split(", ")
        total_salary = sum([salary_mapping[res] for res in responsibilities if res in salary_mapping])
        return total_salary

    def save_account(self): 
        selected_name = self.name_combobox.get()

        allowances = self.allowances_entry.get()

        basic_salary = self.calculate_basic_salary()

        nssf = 0.05 * basic_salary
        paye = 0.10 * basic_salary
        insurance = 0.05 * basic_salary
        tithe = 0.10 * basic_salary

        taxes = nssf + paye + insurance + tithe
        gross_pay = basic_salary  + float(allowances)

        net_pay = gross_pay - float(taxes)


        connection = sqlite3.connect("registration.db")
        cursor = connection.cursor()
        cursor.execute("SELECT employee_id FROM employees WHERE name=?", (selected_name,))
        employee_id = cursor.fetchone()[0]
        connection.close()

        connection = sqlite3.connect("registration.db")
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO account (employee_id, name, responsibilities, basic_salary, taxes, allowances, gross_pay, net_pay)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                            (employee_id, selected_name, self.responsibility_entry.get(), basic_salary, taxes, allowances, gross_pay, net_pay))
        connection.commit()
        print("Account details added successfully.")
if __name__ == "__main__":
    app = addAccountForm()
    app.config(background="white")
    app.mainloop()
