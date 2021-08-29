line = input("Enter a line: ")
lowerCount = upperCount = 0
digitCount = alphaCount = 0
spCharCount = 0
for a in line:
    if a.islower():
        lowerCount += 1
    elif a.isupper():
        upperCount += 1
    elif a.isdigit():
        digitCount += 1
    if a.isalpha():
        alphaCount += 1
    else:
        spCharCount += 1    #space is also counted as special character

print("Number of uppercase letters: ", upperCount)
print("Number of lowercase letters: ", lowerCount)
print("Number of alphabers: ", alphaCount)
print("Number of digits: ", digitCount)
print("Number of special charactres: ", spCharCount)