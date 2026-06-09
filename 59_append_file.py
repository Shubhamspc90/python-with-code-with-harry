f = open("58_text.txt", "a")

data = """
\nThis is a new line added using append mode.
Python file handling is easy to learn.
Appending data does not remove existing content.
"""

f.write(data)

f.close()
print("Data appended successfully.")