string = (input("Enter a string: ")
#length = len(string)
mid = (len(string))/2
rev = -1
for a in range(mid):
    if string[a] == string[rev]:
        a += 1
        rev -= 1
    else:
        print(string, "is not a palindrome.")
        break
else:
    print(string, "is a palindrome.")