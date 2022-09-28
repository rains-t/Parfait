

from tkinter import messagebox
from main import *
from tkinter import *
#new page after logging in 


def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()



class main_page:
    def __init__(self):
        self.root = Tk()
        self.root.title('Main page')
        self.root.geometry('500x500')
        center(self.root)
        #code to have the window be transparent until the movement is complete
        self.root.attributes('-alpha', 1.0)
        
        self.root.mainloop()

class account_creation_page:
    def __init__(self):
        self.root = Tk()
        self.root('Account creation')
        self.root('500x500')
        self.root.mainloop()             

class log_page:

    def __init__(self):
        self.root = Tk()
        self.user_var = StringVar()
        self.pass_var = StringVar()
        self.root.title('log in')
        self.root.geometry('250x100')
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.root.grid_columnconfigure(5, weight=1)

        def get_userpass():
            user = self.user_var.get()
            password = self.pass_var.get()
            print(f"username is: {user}\npassword is:{password}")
            self.user_var.set('')
            self.pass_var.set('')
            if not log_in(user,password):
                messagebox.showerror('', 'Username or password was incorrect.')
            else:
                self.root.destroy()
                main_page()
                

        usernamelbl = Label(self.root, text= 'Username',font=('calibre',10,'bold')).grid(row=0, column=1,sticky='e')
        passwordlbl = Label(self.root, text='Password',font=('calibre',10,'bold')).grid(row=1, column=1,sticky='e')

        username_entry = Entry(self.root,textvariable= self.user_var, width=15).grid(row=0, column=2,sticky='w')
        password_entry = Entry(self.root,show='*',textvariable= self.pass_var, width=15).grid(row=1, column=2,sticky='w')
        login_button = Button(self.root, text= 'Log In', width=10, command=get_userpass).grid(row=2, column=2, sticky='w')    
        center(self.root)
        #code to have the window be transparent until the movement is complete
        self.root.attributes('-alpha', 1.0)
        self.root.mainloop()



if __name__ == "__main__":
    log_page()
        


            

            
        





        