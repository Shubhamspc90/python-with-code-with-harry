# 1. Loop Through Keys

# student = {
#     "name": "Shubham",
#     "age": 21,
#     "course": "MCA"
# }

# for i in student:
#     print(i)
    
#2. Loop Through Values
# student = {
#     "name": "Shubham",
#     "age": 21,
#     "course": "MCA"
# }

# for i in student.values():
#     print(i)

#3. Loop Through Keys Using keys()
# student = {
#     "name": "Shubham",
#     "age": 21,
#     "course": "MCA"
# }

# for i in student.keys():
#     print(i)

#4. Loop Through Key-Value Pairs Using items()
# student = {
#     "name": "Shubham",
#     "age": 21,
#     "course": "MCA"
# }

# for key, value in student.items():
#     print(key, ":", value)

# 5. Print Only Specific Data
student = {
    "name": "Shubham",
    "age": 21,
    "course": "MCA"
}

for key in student:
    print(student[key])