tuple = ('v','a','n','s','h','i','k','a')
char = input("Enter a single letter without quotes:")
if char in tuple:
    count =0
    for a in tuple:
        if a != char:
            count += 1
        else:
            break
    print(char, "is at index", count, "in", tuple)
else:
    print(char, "is NOT IN tuple")