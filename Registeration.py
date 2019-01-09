userinfo = {}

def saveInfo(x,y,z):
    userinfo[x]=y,z

def login():
    name = input("NAME: ")
    if name in userinfo:
        mail_id = input("EMAIL: ")
        password= input("PASSWORD: ")
        if userinfo[name]==(password,mail_id):
            print("Welcome to your dashboard" + " " + name)
            exit()

        else:
            print("Email/Password is incorrect.")

    else:
        print("User is not registered.\n Please Register..")
        register()

def register():

    name = input("Name : ")
    email = input ("Email: ")
    password = input("Password: ")
    if len(password)>= 8:
        saveInfo(name, password, email)
        print("User Info Saved")
    else:
        print("Password too weak. Password should not be less than 8 characters.")


while True:
    print( "Please Login")
    login()


