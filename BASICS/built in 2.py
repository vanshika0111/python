#program to take a real number and convert it to nearest integer and rounds-off to three digit after decimal
num = float(input("Enter a real number: "))
tnum = int(num)   
rnum = round(num)
print("Number", num, "converted to integer in two ways as", tnum, "and", rnum)
rnum2 = round(num,3)   #rounds off to three places after decimal
print(num, "rounded off to 3 places after decimal is", rnum2)