#program to find power a^b

def power(a,b):
	if b==0:
		return 1
	else:
		return a*power(a,b-1)

#main
base = int(input("Enter any positive number: "))
power = int(input("Enter power: "))
result = power(base, power)
print(base, "raised to ", power, "is ", result)