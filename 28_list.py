"""We use a list in Python to store multiple values in a single variable when the data may change.

Lists are:

Ordered
Mutable (can be changed)
Dynamic
Very flexible"""

# List are ordered ,mutable(Changeable )collection of items
marks =[10,20,30,40,50]
print(marks)
print(marks[2])
print(len(marks))
print(max(marks))
print(min(marks))
print(sum(marks))


extra_marks=[2,3,4]

mixed=[20,"shubham", 3.14,True]
print(mixed)
print(mixed[1:3])

# List methods 
print(marks)
marks.append(90)
print(marks)
print(marks.pop())

marks.extend(extra_marks)
print(marks)

my_list=[1,2,5,9,6,4,2]
print(my_list)

my_list.append(100)
print(my_list)

my_list.count(2)
print(my_list)

my_list.insert(3,20)
print(my_list)

my_list.remove(5)
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)

print(my_list.index(9))

fruits = ["apple", "banana", "mango"]

print(fruits.index("banana"))

