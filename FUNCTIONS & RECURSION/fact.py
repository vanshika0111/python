#using for loop
def fact(n):
     fact = 1 
     for i in range(n):
          fact = fact* (i+1)
     return fact
    


#__main__

f= fact(4)
print(f)

#using recusrion
def fact(n):
     if n==1 or n==0:
          return 1 
     else:
          return (n) * fact(n-1)
        
f=int(input("Enter any positive number: "))
print("The factorial of", f, "is", fact(f))