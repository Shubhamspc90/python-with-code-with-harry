# filter() in Python
# filter() is used to select elements from an iterable (list, tuple, etc.) that satisfy a condition.
#Syntax
#filter(function, iterable)
# function returns True or False
# Elements for which the function returns True are kept

#  Example 1: Filter Even Numbers

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))

#  Example 2: Filter Age > 18
ages = [15, 20, 17, 25, 12]

adults = filter(lambda age: age > 18, ages)

print(list(adults))

# Example 3: Without Lambda

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

result = filter(is_even, numbers)

print(list(result))


#  reduce 

"""reduce() in Python

reduce() is used to combine all elements of an iterable into a single value."""

# syntax :
# from functools import reduce
# reduce(function, iterable)

# Example 1: Sum of Numbers
print("Reduce started ")

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)
# its working process
#[1, 2, 3, 4, 5]
#[3, 3, 4, 5]
#[6, 4, 5]
#[10, 5]
#[15]

print(result)

# Example 2: Find Product

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x * y, numbers)

print(result)

# Example 3: Find Maximum
from functools import reduce

numbers = [10, 25, 5, 40, 15]

maximum = reduce(lambda x, y: x if x > y else y, numbers)

print(maximum)

"""What is reduce() in Python?
reduce() is a function from the functools module that repeatedly
applies a function to pairs of elements in an iterable and
reduces the iterable to a single value. It is commonly used for summation,
multiplication, finding maximum/minimum values, and aggregation operations."""

# map()    → Modify each element
# filter() → Select some elements
# reduce() → Return one final value

##Example on [1, 2, 3, 4]:
# map(x*2)        → [2, 4, 6, 8]
# filter(even)    → [2, 4]
# reduce(sum)     → 10