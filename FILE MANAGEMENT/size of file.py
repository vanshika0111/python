#program to find the size of a file in bytes

file = open(r'C:\readme.txt',"r")
str = file.read()
size = len(str)
print("Size of the given file is ", size, "bytes")
file.close()