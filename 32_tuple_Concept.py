
tpl = (1, 2, 3)

# Convert tuple to list
lst = list(tpl)

# Modify the list
lst[0] = 10

# Convert back to tuple
tpl = tuple(lst)

print(tpl)

"""They are:
different tuples,
stored at different memory locations,
with different identities."""

# Proof Using id()
t = (1, 2, 3)
print(id(t))

lst = list(t)
lst[0] = 10

t = tuple(lst)
print(id(t))