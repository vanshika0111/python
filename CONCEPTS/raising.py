# raise in python

#---------------------- CASE 1 ------------
a = input("What is your name? ")
if a.isnumeric():
    raise Exception ("Numbers are not allowed")
print(f"Hello {a}")

b = int(input("Enter your salary: "))
if b==0:
    raise Exception ("Sorry! You have zero balance.")

#---------------------- CASE 2 --------------
c = input("Enter your name: ")
try:
    print(a)   #throws an error as a is not defined
except Exception as e:
    if c=="Solace":
        raise ValueError ("Solace is not alowed. Permission denied.")
    print("Exception is handled")