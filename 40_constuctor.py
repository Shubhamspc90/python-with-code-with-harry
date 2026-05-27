
class Employee:
    
    def __init__(self,name,salary,bond):
       self.name = name
       self.bond = bond
       self.salary = salary
        
    def get_salary(self):
        print(self.salary)
    
    def get_info(self):
        print(f"Name of the Eployee is {self.name} and salary is {self.salary}.And the bond is for {self.bond} years" )
        
e1=Employee("Shubham",200000,5)
e1.get_salary()
e1.get_info()
      
e2=Employee("Dhar",300000,3)
e2.get_info()