

# default Argument 

def greet(name="Shubham"):
    return f"Hello {name} ."

print (greet())

def sum(a,b,plus=20):
    return a+b+plus
print(sum(2,3))
print(sum(2,3,4))

# keyword Argument 

def student(name,age):
    return f"{name} is good student and he is {age} yrs old."

print(student(name="Shubham",age=23))