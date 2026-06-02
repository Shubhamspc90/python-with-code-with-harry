class Employee:
    company="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    # this is Instance method (bydefault)  
    def print_info(self):
        print(f"name of employee is {self.name} and salary is {self.salary}")
        
    # this is static method
    @staticmethod    # if this is not used then if we call the function then it will give an error
    def sum(a,b):
        return a+b
    
    #class method
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
        
    @classmethod
    def print_company(cls):
        print(cls.company)
        
        
        
e1=Employee("Shubham",500000)
e2=Employee("Dhar",120000)
# print(Employee.company)
# print(e1.name," ",e1.salary)
# print(Employee.name)# error

e1.print_info()
e2.print_info()

print(e1.sum(3,8))

print(Employee.company)
e2.change_company("Dell")
print(Employee.company)





        