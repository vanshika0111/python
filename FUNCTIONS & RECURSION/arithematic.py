#function to add 
def add(x,y):
    add = x+y
    return add

#function to subtract
def sub(x,y):
    sub = x-y
    return sub

#function to multiply
def mul(x,y):
    mul = x*y
    return mul

#function to divide
def div(x,y):
    div = x/y
    return div

#function of all operators
#def aeCalc(x,y):
 #   return x+y,x-y,x*y,x/y

#main
one = int(input("Enter first number: "))
two = int(input("Enter second number: "))
addition = add(one,two)
subtraction = sub(one,two)
multiply = mul(one,two)
division = div(one,two)
print("the addition of", one, "and", two, "is", addition)
print("the subtraction of", one, "and", two, "is", subtraction)
print("the multiplication of", one, "and", two, "is", multiply)
print("the division of", one, "and", two, "is", division)