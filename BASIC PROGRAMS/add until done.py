#this program repeatedly asks for numbers untill 'done' is typed and returns the sum of the numbers entered
total = 0
s = input("Enter a number or 'done': ")
while s != 'done':
    number = int(s)
    total = total + number
    s = input("Enter a number or 'done': ")
print("The sum of entered numbers is", total)
