
# class is a blue print or template 
# example:  form for an exam that contain  ,name, age , elective, father name etc
  
# Object : Specific instance that is create from  template class  .
# example : a form that contain the data of shubham chauhan

class Employee:
    company="HP"
    
    def get_Salary(self): # self is important becoz self is the way to reference the object of the class which is being created 
        return 43000


e=Employee()
print(e.get_Salary())
e2=Employee()
print(e2.company)