

from tkinter import messagebox
from main import *
from tkinter import *
#new self.log_page after logging in 
class main_page:
    def __init__(self):
        self.root = Tk()
        self.root.title('Main page')
        self.root.geometry('500x500')
        self.root.mainloop()

class account_creation_page:
    def __init__(self):
        self.root = Tk()
        self.root('Account creation')
        self.root('500x500')
        self.root.mainloop()             

class log_page:

    def __init__(self):
        self.log_page = Tk()
        self.user_var = StringVar()
        self.pass_var = StringVar()
        self.log_page.title('log in')
        self.log_page.geometry('250x100')
        self.log_page.grid_rowconfigure(0, weight=1)
        self.log_page.grid_rowconfigure(1, weight=1)
        self.log_page.grid_rowconfigure(2, weight=1)
        self.log_page.grid_columnconfigure(1, weight=1)
        self.log_page.grid_columnconfigure(2, weight=1)
        self.log_page.grid_columnconfigure(3, weight=1)
        self.log_page.grid_columnconfigure(4, weight=1)
        self.log_page.grid_columnconfigure(5, weight=1)

        def get_userpass():
            user = self.user_var.get()
            password = self.pass_var.get()
            print(f"username is: {user}\npassword is:{password}")
            self.user_var.set('')
            self.pass_var.set('')
            if not log_in(user,password):
                messagebox.showerror('', 'Username or password was incorrect.')
            else:
                self.log_page.destroy()
                main_page()
                

        usernamelbl = Label(self.log_page, text= 'Username',font=('calibre',10,'bold')).grid(row=0, column=1,sticky='e')
        passwordlbl = Label(self.log_page, text='Password',font=('calibre',10,'bold')).grid(row=1, column=1,sticky='e')

        username_entry = Entry(self.log_page,textvariable= self.user_var, width=15).grid(row=0, column=2,sticky='w')
        password_entry = Entry(self.log_page,show='*',textvariable= self.pass_var, width=15).grid(row=1, column=2,sticky='w')
        login_button = Button(self.log_page, text= 'Log In', width=10, command=get_userpass).grid(row=2, column=2, sticky='w')
        self.log_page.mainloop()



if __name__ == "__main__":
    log_page()
        


            

            
        





        