

from tkinter import messagebox
from main import *
from tkinter import *
#new window after logging in       
def main_page():
    window.destroy()
    main_window = Tk()
    new_canvas = Canvas(main_window, height=500, width=500)
    new_canvas.pack()
    main_page.mainloop()

def account_creation_window():
    window.destroy()
    acct_window = Tk()
    acct_window.title('Account creation')
    acct_window.geometry('500x500')

window = Tk()
window.title('Log in')
window.geometry('250x100')
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_columnconfigure(4, weight=1)
window.grid_columnconfigure(5, weight=1)

user_var = StringVar()
pass_var = StringVar()

usernamelbl = Label(window, text= 'Username',font=('calibre',10,'bold')).grid(row=0, column=1,sticky='e')
passwordlbl = Label(window, text='Password',font=('calibre',10,'bold')).grid(row=1, column=1,sticky='e')

username_entry = Entry(window,textvariable= user_var, width=15).grid(row=0, column=2,sticky='w')
password_entry = Entry(window,show='*',textvariable= pass_var, width=15).grid(row=1, column=2,sticky='w')

def get_userpass():
    user = user_var.get()
    password = pass_var.get()
    print(f"username is: {user}\npassword is:{password}")
    user_var.set('')
    pass_var.set('')
    if not log_in(user,password):
        messagebox.showerror('', 'Username or password was incorrect.')
    else:
        main_page()
       

    
login_button = Button(window, text= 'Log In', width=10, command=get_userpass).grid(row=2, column=2, sticky='w')





window.mainloop()

