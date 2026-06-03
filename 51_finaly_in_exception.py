

try:
    print(" for risky code")
except:
    print("for handle exception")
finally:
    print("always runs")
    


try:
    print("Inside try")
except:
    print("Inside except")
finally:
    print("Inside finally")
    
    
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Program finished")