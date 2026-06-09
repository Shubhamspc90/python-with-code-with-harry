with open("58_text.txt", "a") as file:
    data = """
\n
Name: Shubham Chauhan
Course: MCA
Language: Python
Topic: File Handling
Mode Used: Append Mode
"""
    file.write(data)

print("Data appended successfully.")