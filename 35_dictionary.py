"""We use a dictionary (dict) in Python to store data in key-value pairs.

It helps us organize and access data quickly using a key."""

marks={"Shubham" : 90,
       "Dhar": 89}
print(marks,type(marks))

print(marks["Shubham"])
marks["Shubham"]=100
print(marks)