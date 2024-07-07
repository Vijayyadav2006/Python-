def course(a,b,c):
    if(a == "BSC.IT"):
        if(b == "Maths"):
            if(c >=45):
                print("eligible")
            else:
                print("not eligible")
    else:
        print("not eligible")
        
course("BSC.IT","Maths",75)