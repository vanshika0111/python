import random

print("------------ Password Generator -----------")
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*.,?0123456789'
NumberOfPW = int( input ("Enter the number of passwords to generate: "))
Lenght= int( input ("Enter the lenght of password required: "))

print("Use the follwing password(s): \n")
for pwd in range(NumberOfPW):
    password = ''
    for c in range(Lenght):
        password += random.choice(char)
    print(password)