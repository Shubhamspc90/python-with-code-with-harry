import shutil
# shutil.rmtree("dir")    //  it deleted folder name  ( dir)

# shutil.copy("harry.txt","john.txt")  # all the content of harry file is copy to john file

shutil.move("john.txt","shut/")  # john text file move to shut folder from python with code with harry
 
"""Yes, shutil is also a built-in Python module, just like the os module.

Difference Between os and shutil
Module                           	Purpose
os	           Interact with the operating system (files, folders, paths, environment variables, etc.)
shutil	       High-level file and directory operations (copy, move, delete entire folders, 
                archive files, etc.)"""
