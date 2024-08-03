user_name=input("Enter You're Username:")
Password = input("Enter password:")
def login():
    user_entered=input("Enter user name:")
    user_PASS=input("Enter user password:")
    if(user_name == user_entered and Password == user_PASS):
        print("Successfully Login Into a/c")
    else:
        print("Wrong input and password")
        
login()
