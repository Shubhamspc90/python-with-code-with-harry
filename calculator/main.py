try:
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    print('''List of Operation you can perform:
    press + for addition\npress - for substraction\npress * for multiplication\npress /for division''')
    
    o=input("enter operation: ")
    match(o):
        case "+":
            print(f"sum of {a} and {b} = {a+b}")
        case "-":
            print(f"sum of {a} and {b} = {a-b}")
        case "*":
            print(f"sum of {a} and {b} = {a*b}")
        case "/":
            print(f"sum of {a} and {b} = {a/b}")
        case default:
            print("there is an error!")
    
except Exception  as e:
    print("Enter valid no. a and b")