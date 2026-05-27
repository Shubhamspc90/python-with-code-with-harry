

class Employee:
    company="ASUS"
    
    def __init__(self,name,salary,company):
        self.name=name
        self.salary=salary
        self.company=company
    
    def get_info(self):
        print(self.name,self.salary,self.company)
        
e=Employee("shubham",12000,"HP")
e.get_info()
print(Employee.company)