from tkinter import *
import tkinter.messagebox

Win1 = Tk()
Win1.geometry("800x500")

def existing_user():
    info = tkinter.messagebox.askquestion("User Account",'Already have an account?')
    if info =='yes':
        signin()
    else:
        signup()

# Dictionary to hold user information in the format {name:[email,password]
userinfo_db = {}

# User login function
def signin():
    Win1.title("User Login")
    name = StringVar()
    email = StringVar()
    pin = StringVar()
    user_name = Label(Win1, text="NAME:").place(x=10, y=10)
    user_mail = Label(Win1, text="EMAIL:").place(x=10, y=40)
    user_pass = Label(Win1, text="PASSWORD:").place(x=10, y=70)
    name_entry = Entry(Win1, textvariable=name)
    name_entry.place(x=90, y=10)
    mail_entry = Entry(Win1, textvariable=email)
    mail_entry.place(x=90, y=40)
    pass_entry = Entry(Win1, textvariable=pin)
    pass_entry.place(x=90, y=70)


    # verify user details if he is truly registered
    def verify_user():
        names = name.get()
        emails = email.get()
        pins = pin.get()

        while names in userinfo_db:
            if userinfo_db[names]==[emails,pins]:
                Welcome = tkinter.messagebox.showinfo('User Verified', 'Account Verified')
                exit()
            else:
                print("Password/Email is incorrect")
                signin()
        else:
            print('User is not registered. Please register.')
            signup()
    submit = Button(Win1, text="Login", command=verify_user).pack(side=LEFT)

# User signup function
def signup():
    Win1.title("Create an account")
    name = StringVar()
    email= StringVar()
    password=StringVar()
    confirm_password=StringVar()
 # This give syntax error, that is what we want to fix
    user_name = Label(Win1, text="NAME:").place(x=10, y=10)
    user_mail = Label(Win1, text="EMAIL:").place(x=10, y=40)
    user_pass = Label(Win1, text="PASSWORD:").place(x=10, y=70)
    confirm_pass= Label(Win1, text="CONFIRM PASSWORD:").place(x=10, y=100)
    name_entry = Entry(Win1, textvariable=name)
    name_entry.place(x=90, y=10)
    mail_entry = Entry(Win1, textvariable=email)
    mail_entry.place(x=90, y=40)
    pass_entry = Entry(Win1, textvariable=password)
    pass_entry.place(x=90, y=70)
    confirm_password_entry=Entry(Win1, textvariable=confirm_password)
    confirm_password_entry.place(x=140, y=100)

    # save user information into thhe dictionary database
    def save_info():
        get_name = name.get()
        get_email = email.get()
        get_password = password.get()
        get_password2 = confirm_password.get()

        while len(str(password))>=8:
            if get_password == get_password2:
                userinfo_db[get_name]=[get_email,get_password]
                signin()
            else:
                print("Password mismatch")
        else:
            print("Password too weak")



    submit = Button(Win1, text="Register", command=save_info).pack(side=RIGHT)





# Display message box and check for new users
existing_user()



Win1.mainloop()
