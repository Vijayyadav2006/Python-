class Student:
    def _init_(self,name,Sex,Course,result):
        self._name=name
        self._Sex=Sex
        self._course=Course
        self._result=result
        
    def display(self):
            print("Name:",self._name)
            print("Sex:",self._Sex)
            print("Course:",self._course)
            print("result:",self._result)
            
s1=Student("ANC","M","CD",599)
s1.display()
