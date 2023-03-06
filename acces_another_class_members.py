class employee:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.salary=sal
    def printer(self):
        print("Name is ",self.name)
        print("Age is ",self.age)
        print("Salary is ",self.salary)
class changes:
    def increment(obj):
        obj.salary=obj.salary+100000
        obj.printer()
e1=employee("garry", 19,34000)
changes.increment(e1)
