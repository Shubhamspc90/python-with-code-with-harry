

"""Tuple is immutable, so methods like:

append()
remove()
insert()
sort()

do NOT exist for tuples."""

my_tuple = (1, 2, 3, 2, 5)

print(my_tuple.count(2))   # Count occurrences
print(my_tuple.index(5))   # Find index

"""We use tuples in Python when we want to store data that should not change.

A tuple is:

Ordered
Immutable (cannot be modified)
Faster than lists
used as dictinary key(Since they are hashable)
Safer for fixed data"""


# Tuple example

my_tuple = (100, 200, 300, 400)

# loop through tuple
for i in my_tuple:
    print(i)

# Output:
# 100
# 200
# 300
# 400