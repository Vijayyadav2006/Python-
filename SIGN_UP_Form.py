#SIGN UP PAGE 

print("SIGN UP FORM TO FILL FOR REGISTRATION ON WEBSITE")
User_Name=input("Enter User Name:") #user id
Password=input("Enter Password")   #user password
User_Name_Tester=input("Enter you're user name:") 
Password_Tester=input("Enter You're Password:")
if(User_Name_Tester == User_Name):      #condition where we get correct entered password or not
    if(Password == Password_Tester):
        print("Login into a/c")
    else:
        print("Can't Login in A/c",Password_Tester,"incorrect")         
else:
    print("Invalid User Name",User_Name)
    
first_name=input("Enter first name:")#name section
Last_name = input("Enter last name:")

Email_id = input("Enter Email Address:") #email valid or not 
Email_valid = ('gmail.com', 'org.in', 'edu.in', 'gov.in')
if((any(Email_id.endswith(Email_valid))) for Email_valid in Email_valid):
    print("Successful added Email")
else:
    print("Invalid Unsuccessful Login ")
    
Mobile_no=(input("Enter mobile no:")) #mobile no 10 digit condition
mobile_no_eligible=len(Mobile_no)

if Mobile_no and mobile_no_eligible == 10:
   print("Successful added Mobile No:",Mobile_no)
else:
 print("Invalid Mobile No:",Mobile_no,"please enter 10 digit Mobile No")  

Pincode=(input("Enter Pin code ")) #pincode validation
if(len(Pincode) == 6):
    print("Added pin code",Pincode)
else:
    print("Enter correct pin code",Pincode,"Should be 6 digit only accept") 
print([User_Name,Password,first_name,Last_name,Email_id,Mobile_no,Pincode])
