#program to read an entire file

file = open(r'c:\readme.txt',"r")
line = file.readlines()
print(line)
file.close()

#another way
file = open("readme.txt","r")
while str:
	str = file.readline()
	print(str)
file.close()