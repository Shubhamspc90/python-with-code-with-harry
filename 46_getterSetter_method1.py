# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def first_name(self):
#         f_name = self.name.split(" ")
#         return f_name[0]

#     def Set_fname(self, naam):
#         f_name = self.name.split(" ")
#         new_name = f"{naam} {f_name[1]}"
#         self.name = new_name


# e = Employee("Shubham Chauhan", 23)
# print(e.first_name())
# e.Set_fname("Dhar")
# print(e.name)

#  OR  with the help of  propertydecorator and setterand getter

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def first_name(self):
        return self.name.split()[0]

    @first_name.setter
    def first_name(self, naam):
        parts = self.name.split()
        parts[0] = naam
        self.name = " ".join(parts)


e = Employee("Shubham Chauhan", 23)

print(e.first_name)      # getter

e.first_name = "Dhar"    # setter

print(e.name)