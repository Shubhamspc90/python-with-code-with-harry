

def sum(a,b):
    # a,b,c are local variable
    c=a+b
    z=1
    return c

z=5 # here z is global variable
print(z)
print(sum(4,6))
print(z)