num = int(input("Enter any number: "))
prime = True
for i in range(2,num):
     if(num%2==0):
           prime = False
           break
    
if prime:
     print(num, "is prime number.")
else:
     print(num, "is not a prime number.")

    
