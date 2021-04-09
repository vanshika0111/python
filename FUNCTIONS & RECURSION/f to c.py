#This snippet converts temperature from F to C
def fahrenheit(celsius):
         return (celsius*(9/5) + 32)
    
c= float(input("Enter temperature in celsius: "))
f= fahrenheit(c)
print("The temperature in Fahrenheit is",f)