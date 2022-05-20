from tkinter import *
from tkinter import messagebox
import os
import pickle
import empmgmt

d = {}

'''class below defines the main login page which appears when code is executed'''
'''Following code uses class and object'''


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("User Login")
        self.root.geometry("1350x750+0+0")
        '''Frame'''
        self.F1 = Frame(self.root, bd=10, relief=GROOVE)
        self.F1.place(x=450, y=150, height=350)
        # label to show the screen with title Login System
        self.title = Label(self.F1, text="Login System", font=("times new roman", 30, "bold"))
        self.title.grid(row=0, columnspan=2, pady=20)
        '''label'''
        self.lblusername = Label(self.F1, text="Username", font=("times new roman", 25, "bold"))
        self.lblusername.grid(row=1, column=0, pady=10, padx=10)

        self.txtuser = Entry(self.F1, bd=7, relief=GROOVE, width=25, font=("arial 15 bold"))
        self.txtuser.grid(row=1, column=1, padx=10, pady=20)

        self.lblpass = Label(self.F1, text="Password", font=("times new roman", 25, "bold"))
        self.lblpass.grid(row=2, column=0, pady=10, padx=10)

        self.txtpass = Entry(self.F1, bd=7, relief=GROOVE, width=25, font=("arial 15 bold"), show='*')
        self.txtpass.grid(row=2, column=1, padx=10, pady=20)

        '''Button for login, register and exit box'''
        self.btnlog = Button(self.F1, text="Login", font=("arial 15 bold"), bd=7, width=10, command=self.logfun).place(
            x=10, y=250)
        self.btnregister = Button(self.F1, text="Register", font=("arial 15 bold"), bd=7, width=10,
                                  command=self.register).place(x=170, y=250)
        self.btnexit = Button(self.F1, text="Exit", font=("arial 15 bold"), bd=7, width=10,
                              command=self.exit_fun).place(x=330, y=250)

        '''below code executes the data entered from above to login and also validation for valid user name and password'''

    def logfun(self):
        le = os.path.getsize('C:\\Users\\Shishir\\Desktop\\employee\\data.txt')
        if le > 0:
            f = open('data.txt', 'rb+')
            ld = pickle.load(f)
            for i, j in ld.items():
                if i == self.txtuser.get() and j['password'] == self.txtpass.get():
                    res = messagebox.showinfo('success', 'login success')
                    if res == 'ok':
                        self.root.withdraw()
                        empmgmt.File_App()

                    f.close()
                    return
            else:
                messagebox.showerror('error', 'invalid username or password')
                f.close()
        else:
            messagebox.showerror('error', 'file is empty')
    '''function and class to make registration form'''
    def register(self):
        self.root.withdraw()
        a = Toplevel(root)
        Register(a)

    def exit_fun(self):
        option = messagebox.askyesno("Exit", "Do you want to exit?")
        if option > 0:
            self.root.destroy()
        else:
            return

'''class to make a dialogbox of a registration form'''
class Register():
    def __init__(self, root):
        self.root = root
        '''frame'''
        self.frame = LabelFrame(self.root, bd=10, relief=GROOVE)
        self.frame.pack()
        '''label for registration form'''
        self.tt = Label(self.frame, text='Registration Form', font=('times new roman', 20, 'bold'))
        self.tt.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
        '''label to enter name,password and confirm password in entry box'''
        self.lb_name = Label(self.frame, text='Name', font=("times new roman", 20, "bold"))
        self.lb_name.grid(row=1, column=0, padx=20, pady=10, sticky='w')

        self.en_name = Entry(self.frame, bd=7, relief=GROOVE, width=15, font="arial 15 bold")
        self.en_name.grid(row=1, column=1, padx=10, pady=10)

        self.lb_psw = Label(self.frame, text='Password', font=("times new roman", 20, "bold"))
        self.lb_psw.grid(row=2, column=0, padx=20, pady=10, sticky='w')

        self.en_psw = Entry(self.frame, bd=7, relief=GROOVE, show='*', width=15, font="arial 15 bold")
        self.en_psw.grid(row=2, column=1, padx=10, pady=10)

        self.lb_cpsw = Label(self.frame, text='Conform Password', font=("times new roman", 20, "bold"))
        self.lb_cpsw.grid(row=3, column=0, padx=20, pady=10, sticky='w')

        self.en_cpsw = Entry(self.frame, bd=7, relief=GROOVE, width=15, show='*', font=("times new roman", 20, 'bold'))
        self.en_cpsw.grid(row=3, column=1, padx=10, pady=10)
        '''button of confirm box for registration form when data is all filled  '''
        self.button = Button(self.frame, text='Confirm', relief=GROOVE, command=self.register_click)
        self.button.grid(row=5, column=6)
    '''using function to save the data entered in registration and messagebox for validation '''
    def register_click(self):
        if self.en_name.get() == '' or self.en_psw.get() == '' or self.en_cpsw.get() == '':
            messagebox.showerror('Error', 'fill all the values')
        elif self.en_cpsw.get() != self.en_psw.get():
            messagebox.showerror('Error', 'password does not match')
        else:
            global d
            len = os.path.getsize('C:\\Users\\Shishir\\Desktop\\employee\\data.txt')
            username = self.en_name.get()
            password = self.en_psw.get()
            di = {username: {'password': password}}
            '''variable to open the saved data and execute to run in login form '''
            if len > 0:
                f = open('data.txt', 'rb+')
                d = pickle.load(f)
                d.update(di)
                f.seek(0)
                pickle.dump(d, f)
                messagebox.showinfo('success', 'your data was saved')
                f.close()
                self.root.withdraw()
                a = Toplevel(root)
                Login(a)
            else:
                f = open('data.txt', 'wb')
                d.update(di)
                pickle.dump(d, f)
                messagebox.showinfo('success', 'data saved successfully')
                f.close()


root = Tk()
root2 = Tk()
root2.withdraw()
ob = Login(root)
ob2 = Register(root2)
root.mainloop()
