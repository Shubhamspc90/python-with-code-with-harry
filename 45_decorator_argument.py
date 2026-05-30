

def repeat(n):
    def Decorate(funct):
        def wrapper(a):
            for i in range (n):
                funct(a)
        return wrapper
    return Decorate
            
            
            

@repeat(7)
def greet(a):
    print(f"Hello {a}")

greet("Shubham")
    
            