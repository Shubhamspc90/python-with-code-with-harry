# Exception Handling

# while True:
#     try:
#         a=int(input("enter a no. 1 :  "))
#         b=int(input("enter a no. 2:  "))
#         print(f"the division is  = {a/b}")
#     except ValueError:
#         print("please iput numerical values  ")   
#     except ZeroDivisionError:
#         print("Do not divide by zero ") 
#     except Exception as e:
#         print("unknown error Occure ",e)


#  raise error 
a=int(input("enter a no. 1 :  "))
b=int(input("enter a no. 2:  "))
if(b==0):
    raise ValueError("please do not divide by Zero")

print(f"the division is  = {a/b}")