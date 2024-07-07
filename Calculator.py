def add(a,b):
    return a+b
def sub(a,b):
    return a-b  
def multiple(a,b):
    return a*b
    
def divide(a,b):
    return a/b
    
c =int(input('''Enter
                  1: "add"
                  2: "subtract"
                  3:"multiply"
                  4:"divide"
                  '''))
                  
no1=int(input("enter 1's no:"))
no2=int(input("enter 2'nd no:"))
if(c == 1):
   a=add(no1,no2)
   print(a)
elif(c == 2):
    b=sub(no1,no2)
    print(b)
elif(c == 3):
    c=multiple(no1,no2)
    print(c)
elif(c == 4):
    d=divide(no1,no2)
    print(d)