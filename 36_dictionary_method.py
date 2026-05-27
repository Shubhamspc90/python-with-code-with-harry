
"""Characteristics of Dictionary
Stores data in key-value form
Mutable (can change)
Duplicate keys not allowed"""


# Dictionary methods example

student = {
    "name": "Shubham",
    "age": 21,
    "course": "MCA"
}

print(student)

# -------------------------------------------------

# get() -> gets value using key
print(student.get("name"))
# Output: Shubham

# -------------------------------------------------

# keys() -> returns all keys
print(student.keys())
# Output: dict_keys(['name', 'age', 'course'])

# -------------------------------------------------

# values() -> returns all values
print(student.values())
# Output: dict_values(['Shubham', 21, 'MCA'])

# -------------------------------------------------

# items() -> returns key-value pairs
print(student.items())
# Output: dict_items([('name', 'Shubham'), ('age', 21), ('course', 'MCA')])

# -------------------------------------------------

# update() -> updates dictionary
student.update({"city": "Ghaziabad"})
print(student)

# Output:
# {'name': 'Shubham', 'age': 21, 'course': 'MCA', 'city': 'Ghaziabad'}

# -------------------------------------------------

# pop() -> removes element using key
student.pop("age")
print(student)

# Output:
# {'name': 'Shubham', 'course': 'MCA', 'city': 'Ghaziabad'}

# -------------------------------------------------

# copy() -> creates copy of dictionary
new_student = student.copy()

print(new_student)

# Output:
# {'name': 'Shubham', 'course': 'MCA', 'city': 'Ghaziabad'}

# -------------------------------------------------

# clear() -> removes all elements
temp = {
    "a": 1,
    "b": 2
}

temp.clear()

print(temp)

# Output:
# {}