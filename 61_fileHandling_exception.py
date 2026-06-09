try:
    with open("58_text.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

except Exception as e:
    print("Error:", e)

finally:
    print("File operation completed.")