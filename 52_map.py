# 1. map in Python
# map() applies a function to every element of an iterable (list, tuple, etc.).
#Syntax
#map(function, iterable)
print("using lambda method")
numbers = [1, 2, 3, 4]
print(numbers)

result = map(lambda x: x * 2, numbers)

print(list(result))

print( "using simple method ")
num = [ 3, 4 ,5 ,6]
print(num)
def square(x):
    return x*x

new_list=map(square,num)
print(list(new_list))