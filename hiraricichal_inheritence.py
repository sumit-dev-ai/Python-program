class Person:
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag
    def display(self):
        print("Person class called")
class Emloyee(Person):
    def __init__(self,nm,ag,sal):
        super().__init__(nm,ag)
        self.salary=sal
    def display(self):
        print("emplyee clas called ")
class student(Person):
    def __init__(self, nm, ag,m):
        super().__init__(nm, ag)
        self.marks=m
    def display2(self):
        print("student class called")
s=student("rajul" ,21, 90)
s.display2()
