""""""
# tuples are ordered but immutable(means can not be change after creation)

my_tuple=(1,2,3)
print(my_tuple)

single_element=(5)
print(single_element)
print(type(single_element)) # <class 'int'>

single_ele=(5,)
print(single_ele)
print(type(single_ele)) # <class 'tuple'>

# tuple Unpacking

tu=(10,20,30)
a,b,c = tu
print(a,b,c)