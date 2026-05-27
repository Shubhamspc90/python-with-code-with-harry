# Set methods example

s = {10, 38, 48, 45, 76}
print(s)  
# Output: {48, 38, 10, 76, 45}

# add() -> adds single element
s.add(222)
print(s)  
# Output: {48, 38, 10, 76, 45, 222}

# add() -> adds another element
s.add(888)
print(s)  
# Output: {48, 38, 888, 10, 76, 45, 222}

# pop() -> removes random element
s.pop()
print(s)

# remove() -> removes specified element ,error if not found
s.remove(38)
print(s)

# discard() -> removes element, no error if not found
s.discard(100)
print(s)

# update() -> adds multiple elements
s.update([500, 600, 700])
print(s)

# copy() -> creates copy of set
new_set = s.copy()
print(new_set)

# clear() -> removes all elements
temp = {1, 2, 3}
temp.clear()
print(temp)  
# Output: set()

#  Sets Operation -------------------------------------------------

# union() -> combines both sets
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))  
# Output: {1, 2, 3, 4, 5}

# intersection() -> common elements
print(a.intersection(b))  
# Output: {3}

# difference() -> elements only in first set
print(a.difference(b))  
# Output: {1, 2}

# symmetric_difference() -> uncommon elements
print(a.symmetric_difference(b))  
# Output: {1, 2, 4, 5}

# -------------------------------------------------

# issubset() -> checks all elements exist or not
x = {1, 2}
y = {1, 2, 3, 4}

print(x.issubset(y))  
# Output: True

# issuperset() -> checks set contains all elements
print(y.issuperset(x))  
# Output: True

# isdisjoint() -> checks no common elements
m = {11, 22}
n = {33, 44}

print(m.isdisjoint(n))  
# Output: True

# -------------------------------------------------

# difference_update() -> removes common elements
p = {1, 2, 3, 4}
q = {3, 4}

p.difference_update(q)
print(p)  
# Output: {1, 2}

# intersection_update() -> keeps only common elements
r = {1, 2, 3, 4}
t = {2, 3, 5}

r.intersection_update(t)
print(r)  
# Output: {2, 3}

# symmetric_difference_update() -> keeps uncommon elements
u = {1, 2, 3}
v = {3, 4, 5}

u.symmetric_difference_update(v)
print(u)  
# Output: {1, 2, 4, 5}