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
        
x=int(input("Enter the first number:"))
y=int(input("Enter 2nd number:"))
c1=Calculator(x,y)
c1.add()
c1.sub()
c1.multiply()
c1.division()
