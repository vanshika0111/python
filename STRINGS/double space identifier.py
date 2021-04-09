#This programs returns the index value where double space occure else it returns -1

a = "This program enables you to find if the string conatins  double space!"
#a = "This program enables you to find if the string conatins double space!"

double_space = a.find("  ")
print(double_space)

#now the further code replaces double space (if any) with single space
a = a.replace("  "," ")
print(a)