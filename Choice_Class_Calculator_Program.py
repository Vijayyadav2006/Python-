class Calculator:
    def _init_(self,a,b):
        self.no1=a
        self.no2=b
    def add(self):
        print("add=",self.no1+self.no2)
    def sub(self):
        print("sub=",self.no1-self.no2)    
    def multiply(self):
        print("multiply=",self.no1*self.no2)    
    def division(self):
        print("division=",self.no1/self.no2)
    def remainder(self):
        print("remainder=",self.no1%self.no2)
        
        
        
x=int(input("Enter the first number:"))
y=int(input("Enter 2nd number:"))
c1=Calculator(x,y)
        
choice = int(input('''Enter The Choice Wants To Perform
        1.Addition
        2.Subtraction
        3.Multiplacation
        4.Division
        5.Remainder:'''))

if  choice ==1:
    c1.add()
elif choice ==2:
    c1.sub()
elif choice ==3:
    c1.multiply()
elif choice ==4:
    c1.division()
elif choice ==5:
    c1.remainder()
else:
    print("Trying to perform Wrong Operation")
