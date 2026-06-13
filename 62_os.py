

# ==========================================
# Python OS Module - Complete Example
# ==========================================

import os

# ------------------------------------------
# 1. Get Current Working Directory
# ------------------------------------------
print("Current Directory:")
print(os.getcwd())

# ------------------------------------------
# 2. Change Directory
# (Uncomment and provide valid path)
# ------------------------------------------
# os.chdir("C:/Users/Username/Documents")
# print("New Directory:", os.getcwd())

# ------------------------------------------
# 3. List Files and Folders
# ------------------------------------------
print("\nFiles and Folders:")
print(os.listdir())

# ------------------------------------------
# 4. Create a New Directory
# ------------------------------------------
folder_name = "DemoFolder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"\nFolder '{folder_name}' created.")
else:
    print(f"\nFolder '{folder_name}' already exists.")

# ------------------------------------------
# 5. Create Nested Directories
# ------------------------------------------
nested_path = "Parent/Child/GrandChild"

if not os.path.exists(nested_path):
    os.makedirs(nested_path)
    print("Nested directories created.")

# ------------------------------------------
# 6. Rename a Folder
# ------------------------------------------
if os.path.exists("DemoFolder"):
    os.rename("DemoFolder", "RenamedFolder")
    print("Folder renamed to 'RenamedFolder'.")

# ------------------------------------------
# 7. Check Path Information
# ------------------------------------------
path = "RenamedFolder"

print("\nPath Information:")
print("Exists:", os.path.exists(path))
print("Is File:", os.path.isfile(path))
print("Is Directory:", os.path.isdir(path))

# ------------------------------------------
# 8. Get Absolute Path
# ------------------------------------------
print("\nAbsolute Path:")
print(os.path.abspath(path))

# ------------------------------------------
# 9. Join Paths
# ------------------------------------------
joined_path = os.path.join("folder", "subfolder", "file.txt")

print("\nJoined Path:")
print(joined_path)

# ------------------------------------------
# 10. Environment Variables
# ------------------------------------------
print("\nPATH Environment Variable:")
print(os.environ.get("PATH"))

# Create a custom environment variable
os.environ["MY_NAME"] = "Shubham"

print("\nCustom Environment Variable:")
print(os.environ.get("MY_NAME"))

# ------------------------------------------
# 11. Get Operating System Name
# ------------------------------------------
print("\nOperating System:")
print(os.name)

# nt    -> Windows
# posix -> Linux/Mac

# ------------------------------------------
# 12. Execute System Command
# ------------------------------------------
print("\nExecuting System Command:")

if os.name == "nt":
    os.system("dir")  # Windows
else:
    os.system("ls")   # Linux/Mac

# ------------------------------------------
# 13. Walk Through Directories
# ------------------------------------------
print("\nDirectory Tree:")

for root, dirs, files in os.walk("."):
    print("\nCurrent Folder:", root)
    print("Subfolders:", dirs)
    print("Files:", files)

# ------------------------------------------
# 14. File Path Operations
# ------------------------------------------
sample_path = "folder/file.txt"

print("\nPath Operations:")
print("Base Name :", os.path.basename(sample_path))
print("Directory :", os.path.dirname(sample_path))
print("Absolute  :", os.path.abspath(sample_path))

# ------------------------------------------
# 15. Remove Directories
# (Uncomment if you want to delete)
# ------------------------------------------

# os.rmdir("RenamedFolder")
# print("RenamedFolder deleted.")

# os.removedirs("Parent/Child/GrandChild")
# print("Nested directories deleted.")

print("\nProgram Completed Successfully!")