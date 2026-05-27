# Strings are immutable.
"""name = "Shubham"
name[0] = "R"   # Error"""
t="Shubham Chauhan"
# len() get the lenght of string 
print(len(t))  #  15
print(t.count("h"))  # 4  count the no. of apperence
 
# Concatination 
p1="Hello"
p2="World"
print(p1,p2)
print(p1+" "+p2)

# changing Case
t1= "hello world"
print (t1)
print(t1.upper(),t1) #  HELLO WORLD hello world
print(t1.lower())  #  hello world
print(t1.capitalize())  #  Hello world
print(t1.title())  #  Hello world

# Removing Whitespace 

t2= "  hello   world   "
print (t2)
print(t2.strip()) # "hello howld"
print(t2.lstrip())  # "hello howld   "
print(t2.rstrip())  # "   hello howld"

# finding and Replacing 
t3= "python is fun"
print(t3.find("f"))  #  10
print(t3.replace("fun"," Amazing"))  #  python is  Amazing

# spliting and joining
t4="Apple,Orange,Pineapple"
print(t4.split(","))  #  ['Apple', 'Orange', 'Pineapple']
print(",".join(['Apple', 'Orange', 'Pineapple']))    #  Apple,Orange,Pineapple

# Chaeking string Properties
t5 = "python123"
print(t5.isalnum())
print(t5.isalpha)
print(t5.isdigit())
print(t5.isspace())
"""True
<built-in method isalpha of str object at 0x0000026CE1920330>
False
False"""

# Character incoding
print(ord('A'))
print(chr(65))