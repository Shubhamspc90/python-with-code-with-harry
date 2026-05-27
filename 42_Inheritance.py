

class Animal:
    location ="Australia"
    
    def __init__(self,name):
        self.name=name
        
    def sound(self):
        print ("generic sound of animal")
        
class Dog(Animal):
    def sound (self):
        super().sound()#  if we want to use method of parent class by using object of child class
        print("Bark..")
        

A=Animal("brabo")
A.sound()
print(A.location)    
   
d=Dog("Bruno")
d.sound()
print(d.location)

d.sound()
