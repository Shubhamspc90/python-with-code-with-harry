

class Animal:
    
    def sound(self):
        print("Some sound..")
        
class Dog(Animal):
    def sound(self):
        print("Bark ...")
        
a=Animal()
a.sound()       
d=Dog()
d.sound()