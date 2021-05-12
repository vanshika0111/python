#program to find greatest common divisor of two numbers

def gcd(a,b):
	if(b==0):
		return a
	else:
		return gcd(b, a%b)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
answer = gcd(n1,n2)
print("GCD of ", n1, "and", n2, "is ", answer)