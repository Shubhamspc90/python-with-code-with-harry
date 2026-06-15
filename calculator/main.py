try:
    while(True):
        choice=input(("press 'q' to quit or Press Enter to continue."))
        if choice.lower()=='q':
            print("Program Exited Successfully")
            break
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))
        print('''List of Operation you can perform:
        press + for addition\npress - for substraction\npress * for multiplication\npress /for division''')
        
        o=input("enter operation: ")
        match o:
            case "+":
                print(f"sum of {a} and {b} = {a+b}")
            case "-":
                print(f"sum of {a} and {b} = {a-b}")
            case "*":
                print(f"sum of {a} and {b} = {a*b}")
            case "/":
                print(f"sum of {a} and {b} = {a/b}")
            case _:
                print("wrong operator!")
    
except ValueError:
    print("Enter valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")