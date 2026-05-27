
# create a list that contain table of 5

# table=[]
# for i in range (1,11):
#     table.append(5*i)
    
# print(table)

# OR through list comprehension  
table=[5*i for i in range(1,11)]
print(table)

# square
square=[ 2**i for i in range (1,14)]
print(square)

# cube
square=[ 3**i for i in range (1,12)]
print(square)

 
# List example

my_list = [10, 20, 30, 40]

# loop through list
for i in my_list:
    print(i)

# Output:
# 10
# 20
# 30
# 40