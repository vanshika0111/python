#program to receive an octal number and print the equivalent number in other number bases using function

def octToOthers(n):
    print("Octal number: ",n)
    numString = str(n)
    decNumb = int(numString,8)
    print("Number in decimal: ", decNumb)
    print("Number in binary: ", bin(decNumb))
    print("Number in hexadecimal: ", hex(decNumb))

#main
number = int(input("Enter an octal number: "))
octToOthers(number)

