# ============================
# WITHOUT WALRUS OPERATOR
# ============================
# 1. Taking Input and Using It
name = input("Enter name: ")

if name:
    print("Hello", name)


# ============================
# WITH WALRUS OPERATOR
# ============================

if (name := input("Enter name: ")):
    print("Hello", name)
    
   
   
   
   
# #    2. Length of List 
# # ============================
# # WITHOUT WALRUS OPERATOR
# # ============================

# numbers = [1, 2, 3, 4, 5]

# n = len(numbers)

# if n > 3:
#     print("Length =", n)


# # ============================
# # WITH WALRUS OPERATOR
# # ============================

# numbers = [1, 2, 3, 4, 5]

# if (n := len(numbers)) > 3:
#     print("Length =", n)
    
    
# # 3. While Loop Input
# # ============================
# # WITHOUT WALRUS OPERATOR
# # ============================

# data = input("Enter value: ")

# while data != "quit":
#     print("You entered:", data)
#     data = input("Enter value: ")


# # ============================
# # WITH WALRUS OPERATOR
# # ============================

# while (data := input("Enter value: ")) != "quit":
#     print("You entered:", data)
    
    
    
    
# # 4. Reading File Line by Line
# # ============================
# # WITHOUT WALRUS OPERATOR
# # ============================

# file = open("test.txt")

# line = file.readline()

# while line:
#     print(line.strip())
#     line = file.readline()

# file.close()


# # ============================
# # WITH WALRUS OPERATOR
# # ============================

# file = open("test.txt")

# while (line := file.readline()):
#     print(line.strip())

# file.close()




# # 5. List Comprehension
# # ============================
# # WITHOUT WALRUS OPERATOR
# # ============================

# numbers = [1, 2, 3, 4, 5]

# result = []

# for num in numbers:
#     square = num * num

#     if square > 10:
#         result.append(square)

# print(result)


# # ============================
# # WITH WALRUS OPERATOR
# # ============================

# numbers = [1, 2, 3, 4, 5]

# result = [
#     square
#     for num in numbers
#     if (square := num * num) > 10
# ]

# print(result)


# # 6. Regular Assignment vs Walrus
# # ============================
# # NORMAL ASSIGNMENT
# # ============================

# x = 10

# print(x)


# # ============================
# # WALRUS ASSIGNMENT
# # ============================

# print(x := 10)