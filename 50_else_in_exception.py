# esle , finally in Exception handling 

# a=2/0
# print(a)  # zero division error

try:
    a=2/0
    print(a)
    
except Exception as e:
    print(e)
    
else :
    print("I am shubham chauhan ")  # only excuted  when there is no error in try block
    
    
    
age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")