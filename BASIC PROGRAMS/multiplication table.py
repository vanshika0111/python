#This snippet displays the multiplication table of any desired number
number = int(input("Enter any number: "))

for i in range(1,11):
    print( str(number) + "X" + str(i) + "=" + str(i*number))
    print(f"{number}X{i}={number*i}")  #fstring