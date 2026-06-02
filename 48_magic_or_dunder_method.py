
class Employee:
    company="HP"
    # magic methods  or Dunder method (it include double underscore) 
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    # magic methods   or Dunder method (it include double underscore) 
    def __str__(self):
        return f"the name of employee is {self.name} and age is {self.age}"
    # magic methods  or Dunder method (it include double underscore) 
    def __repr__(self):
        return f"name : {self.name} \nage : {self.age}"
    # magic methods   or Dunder method (it include double underscore) 
    def __len__(self):
        return len(self.name)
        
        
e=Employee("shubham",7)
# print(e.name)
# print(e.age)
# print(e.name,e.age)
# print(str(e))
# print(repr(e))

print(len(e))

