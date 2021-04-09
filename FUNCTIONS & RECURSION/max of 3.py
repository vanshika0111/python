#This snippet finds the maximum of entered three numbers
def max(num1,num2,num3):
     if(num1 > num2):
          if(num2 > num3):
               return num1
          else:
               return num3
     else:
          if(num2 > num3):
               return num2
          else:
               return num3
   
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
maximum = max(a,b,c)
print("The maximum of",a,b,c, "is",maximum)