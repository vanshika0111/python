#program to reverse a string

def reverse(str,n):
	if n>0:
		print(str[n], end='')
		reverse(str,n-1)
	elif n==0:
		print(str[0])

#main
string = input("Enter a string: )
reverse(s, len(s)-1)