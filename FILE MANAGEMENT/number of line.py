#program to find the number of lines in the file

file = open(r'c:\readme.txt',"r")
line = file.readlines()
lineCount = len(s)
print("Number of lines in the file is ", lineCount)
file.close()