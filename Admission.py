Course = input("enter the course Want:")
if(Course == "BSC.IT"):
    Percentage =int(input("Enter You're Percentage"))
    Sub = input("Enter option Subject Name:")
    if(Sub =="Maths"):
        if(Percentage >=55):
            print("Successful Admission")
        else:
            print("Not Eligible")

else:
    print("Not Eligible")
print("Admission Department")