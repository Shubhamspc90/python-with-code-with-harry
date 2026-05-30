
# A Decorator is a function that adds extra functionality to another function without modifying its original code.
#decorator is a function that take function ,its create new function inside its body(Wrapper),then it returns that new function 

    
def Decorator_function(func):
    def wrapper():
        print("I am going to execute this function..")
        func()
        print("I have excetuted this function..")
        
    return wrapper
@Decorator_function       
def greet():
    print ("hello")   
greet()
# d=Decorator_function(greet)
# d()


#or  jusr remove @Decorator_function  and comment the greet() and uncomment  d=Decorator_function(greet), d()







