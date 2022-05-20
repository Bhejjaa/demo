from tkinter import *
from tkinter import ttk, messagebox
import os

'''class and function of employee management system'''
class File_App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Employee Management System")
        self.root.geometry("1350x700+0+0")

        '''label and frame for EMS messagebox'''

        title = Label(self.root, text="Employee Management System",bd=10, relief=GROOVE, pady=10, font=("times new roman", 35, "bold")).pack(fill=X)

        Employee_Frame = Frame(self.root, bd=10, relief=GROOVE)
        Employee_Frame.place(x=20, y=100, height=410)

        Etitle = Label(Employee_Frame, text="Employee Details", font=("times new roman", 30, "bold")).grid(row=0, columnspan=4, pady=20)

        # =============All Variables=============#
        self.e_id = StringVar()
        self.name = StringVar()
        self.address = StringVar()
        self.salary = StringVar()
        self.qualification = StringVar()
        self.contact = StringVar()
        self.dateofbirth = StringVar()
        self.department = StringVar()
        self.paymode = StringVar()
        self.idproof = StringVar()

        '''label,frame,grid to create box for employee details to save'''

        self.lblEid = Label(Employee_Frame, text="Employee ID", font=("times new roman", 20, "bold"))
        self.lblEid.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        self.txteid = Entry(Employee_Frame, bd=7, textvariable=self.e_id, relief=GROOVE, width=15,font="arial 15 bold")
        self.txteid.grid(row=1, column=1, padx=10, pady=10)

        self.lblcontact = Label(Employee_Frame, text="Contact No.", font=("times new roman", 20, "bold"))
        self.lblcontact.grid(row=1, column=2, pady=10, padx=20, sticky="w")
        self.txtcontact = Entry(Employee_Frame, bd=7, textvariable=self.contact, relief=GROOVE, width=15,font="arial 15 bold")
        self.txtcontact.grid(row=1, column=3, padx=10, pady=10)

        self.lblname = Label(Employee_Frame, text="Name", font=("times new roman", 20, "bold"))
        self.lblname.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        self.txtname = Entry(Employee_Frame, bd=7, textvariable=self.name, relief=GROOVE, width=15,font="arial 15 bold")
        self.txtname.grid(row=2, column=1, padx=10, pady=10)

        self.lbldate = Label(Employee_Frame, text="DOB(dd/mm/yyyy)", font=("times new roman", 20, "bold"))
        self.lbldate.grid(row=2, column=2, pady=10, padx=20, sticky="w")
        self.txtdate = Entry(Employee_Frame, bd=7, textvariable=self.dateofbirth, relief=GROOVE, width=15,font="arial 15 bold")
        self.txtdate.grid(row=2, column=3, padx=10, pady=10)

        self.lblAddress = Label(Employee_Frame, text="Address", font=("times new roman", 20, "bold"))
        self.lblAddress.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        self.txtAddress = Entry(Employee_Frame, bd=7, textvariable=self.address, relief=GROOVE, width=15,font="arial 15 bold")
        self.txtAddress.grid(row=3, column=1, padx=10, pady=10)

        self.lblDepartment = Label(Employee_Frame, text="Department", font=("times new roman", 20, "bold"))
        self.lblDepartment.grid(row=3, column=2, pady=10, padx=20, sticky="w")

        self.lblSalary = Label(Employee_Frame, text="Salary", font=("times new roman", 20, "bold"))
        self.lblSalary.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        self.txtSalary = Entry(Employee_Frame, bd=7, textvariable=self.salary, relief=GROOVE, width=15,font="arial 15 bold")
        self.txtSalary.grid(row=4, column=1, padx=10, pady=10)

        self.lblPayMode = Label(Employee_Frame, text="Payment Mode", font=("times new roman", 20, "bold"))
        self.lblPayMode.grid(row=4, column=2, pady=10, padx=20, sticky="w")

        self.lblQualification = Label(Employee_Frame, text="Qualification", font=("times new roman", 20, "bold"))
        self.lblQualification.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        self.txtQualification = Entry(Employee_Frame, bd=7, textvariable=self.qualification, relief=GROOVE, width=15,font="arial 15 bold")
        self.txtQualification.grid(row=5, column=1, padx=10, pady=10)

        self.lblIdProof = Label(Employee_Frame, text="ID Proof", font=("times new roman", 20, "bold"))
        self.lblIdProof.grid(row=5, column=2, pady=10, padx=20, sticky="w")

        '''combobox for department, paymode and idproof'''

        self.Departmentcombo = ttk.Combobox(Employee_Frame, textvariable=self.department, width=15, state="readonly", font="arial 15 bold")
        self.Departmentcombo['values'] = ("Chair Man", "Principal", "Lecturer", "Accountant", "Front Desk", "Helper", "Staffs")
        self.Departmentcombo.grid(row=3, column=3, padx=10, pady=10)

        self.PayModecombo = ttk.Combobox(Employee_Frame, textvariable=self.paymode, width=15, state="readonly", font="arial 15 bold")
        self.PayModecombo['values'] = ("Cash", "Bank Deposit", "Cheque", "Esewa")
        self.PayModecombo.grid(row=4, column=3, padx=10, pady=10)

        self.IdProofcombo = ttk.Combobox(Employee_Frame, textvariable=self.idproof, width=15, state="readonly", font="arial 15 bold")
        self.IdProofcombo['values'] = ("CitizenShip ID", "Driving License", "Passport")
        self.IdProofcombo.grid(row=5, column=3, padx=10, pady=10)

        '''frame button for save,delete,clear,logout and exit'''

        btnFrame = Frame(self.root, bd=10, relief=GROOVE)
        btnFrame.place(x=10, y=560)

        btnsave = Button(btnFrame, text="Save", font="arial 15 bold",bd=7, width=18, command=self.save_data).grid(row=0, column=0, padx=12, pady=10)
        btndelete = Button(btnFrame, text="Delete", command=self.delete, font="arial 15 bold",bd=7, width=18).grid(row=0, column=1, padx=12, pady=10)
        btnclear = Button(btnFrame, text="Clear", command=self.clear, font="arial 15 bold", bd=7, width=18).grid(row=0, column=2, padx=12, pady=10)
        btnlog = Button(btnFrame, text="Logout", command=self.logout, font="arial 15 bold",bd=7, width=18).grid(row=0, column=3, padx=12, pady=10)
        btnexit = Button(btnFrame, text="Exit", command=self.exit_fun, font="arial 15 bold",bd=7, width=18).grid(row=0, column=4, padx=12, pady=10)

        File_Frame = Frame(self.root, bd=10, relief=GROOVE)
        File_Frame.place(x=1030, y=100, width=300, height=410)

        '''label , scroll bar ,list to make a box in side of the program to show the entered data of the employee'''

        ftitle = Label(File_Frame, text="All Files", font="arial 20 bold", bd=5, relief=GROOVE).pack(side=TOP, fill=X)

        scroll_y = Scrollbar(File_Frame, orient=VERTICAL)
        self.file_list = Listbox(File_Frame, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH, expand=1)
        self.file_list.bind("<ButtonRelease-1>", self.get_data)
        self.show_files()

        self.root.mainloop()
    '''function,loop ,messagebox and validation for the details entered in above code'''
    def save_data(self):
        present = "no"
        if self.txteid.get() == "":
            messagebox.showerror("Error", "Employee ID must be Required!!!")
        else:
            f = os.listdir("C:/files/")
            if len(f) > 0:
                for i in f:
                    if i.split(".")[0] == self.txteid.get():
                        present = "yes"
                if present == "yes":
                    ask = messagebox.askyesno("Update", "File already Present\n Do you want to update it?")
                    if ask > 0:
                        self.save_files()
                        messagebox.showinfo("Update", "Record has been updated Successfully")
                        self.show_files()

                else:
                    self.save_files()
                    messagebox.showinfo("Update", "Record has been updated Successfully")
                    self.show_files()
            else:
                self.save_files()
                messagebox.showinfo("Update", "Record has been updated Successfully")
                self.show_files()
    '''string variable in function to save the files entered above as well as saving combobox '''
    def save_files(self):
        f = open("C:/files/" + str(self.txteid.get()) + ".txt", "w")
        f.write(
            str(self.txteid.get()) + "," +
            str(self.txtname.get()) + "," +
            str(self.txtAddress.get()) + "," +
            str(self.txtSalary.get()) + "," +
            str(self.txtQualification.get()) + "," +
            str(self.txtcontact.get()) + "," +
            str(self.txtdate.get()) + "," +
            str(self.Departmentcombo.get()) + "," +
            str(self.PayModecombo.get()) + "," +
            str(self.IdProofcombo.get()) + ","
        )
        f.close()
    '''function to show the files from the path of txt file created from entering the details of employee '''
    def show_files(self):
        files = os.listdir("C:/files/")
        self.file_list.delete(0, END)
        if len(files) > 0:
            for i in files:
                self.file_list.insert(END, i)
    '''funtion to get the data saved from the path in the system'''
    def get_data(self, ev):
        self.clear()
        get_cursor = self.file_list.curselection()
        # print(self.file_list.get(get_cursor))
        f1 = open("C:/files/" + self.file_list.get(get_cursor))
        value = []
        for f in f1:
            value = f.split(",")
        self.txteid.insert(0, value[0])
        self.txtname.insert(0,value[1])
        self.txtAddress.insert(0,value[2])
        self.txtSalary.insert(0,value[3])
        self.txtQualification.insert(0,value[4])
        self.txtcontact.insert(0,value[5])
        self.txtdate.insert(0,value[6])
        print(value[7], value[8], value[9])
        self.Departmentcombo.set(value[7])
        self.PayModecombo.set(value[8])
        self.IdProofcombo.set(value[9])
    '''function to clear the saved data to fill the new one'''
    def clear(self):
        self.txteid.delete(0, 'end')
        self.txtname.delete(0, 'end')
        self.txtAddress.delete(0, "end")
        self.txtSalary.delete(0, "end")
        self.txtQualification.delete(0, "end")
        self.txtcontact.delete(0, "end")
        self.txtdate.delete(0, "end")
        self.Departmentcombo.set("")
        self.PayModecombo.set("")
        self.IdProofcombo.set("")
    '''function to delete the saved data and if else statement used for validation'''
    def delete(self):
        present = "no"
        if self.txteid.get() == "":
            messagebox.showerror("Error", "Employee ID must be Required!!!")
        else:
            f = os.listdir("C:/files/")
            if len(f) > 0:
                for i in f:
                    if i.split(".")[0] == self.txteid.get():
                        present = "yes"
                if present == "yes":
                    ask = messagebox.askyesno("Delete", "Do you really want to Delete?")
                    if ask > 0:
                        os.remove("C:/files/" + self.txteid.get() + ".txt")
                        messagebox.showinfo("Success", "Deleted Successfully")
                        self.clear()
                        self.show_files()
                    else:
                        messagebox.showerror("Error", "File not Found")
    '''function for exit button and messagebox to make sure '''
    def exit_fun(self):
        ask = messagebox.askyesno("Exit", "Do you really want to exit?")
        if ask > 0:
            self.root.destroy()
    '''function for exit from the system'''
    def logout(self):
        self.root.destroy()