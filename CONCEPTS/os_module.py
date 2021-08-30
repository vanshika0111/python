# os module (built-in module)

import os

# to display all the attributes of os module
print(dir(os))

# to view the cirrent working directory
print(os.getcwd())

# to change directory
os.chdir("C://")
print(os.getcwd())
# f= open("demo.txt")  --> throws an error as the dir is changed

# to list the files of a dir
print(os.listdir("C://"))
print(type(os.listdir("C://")))

# to make a folder 
os.mkdir("This")

# to make multiple folders
os.makedirs("This/That")

# to rename a dir
os.rename("demo.txt", "bye.txt")

# to read environmental variables
print(os.environ.get('Path'))

# to join two different paths
print(os.path.join("C://", "bye.txt"))

# to check if path/dir exists
print(os.path.exists("C://"))

# to check if it is a file
print(os.path.isfile("C://"))

# to check if it is a dir
print(os.path.isdir("C://"))