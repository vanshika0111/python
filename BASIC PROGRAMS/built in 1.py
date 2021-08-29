#program to read a number and convert into octal and hexadecimal using built-in function
number = int(input("Enter a number: "))
print("Number entered = ",number)
octal = oct(number)
hexa = hex(number)
print("The octal conversion is ", octal)
print("The hexadecimal conversion is ", hexa)