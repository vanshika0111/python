#program to generate 4 terms of arithmatic progression

def ap(first,cd):
    return first, first+cd, first+2*cd, first+3*cd

#main
first = int(input("Enter first term of AP: "))
cd = int(input("Enter common difference of AP: "))
print("AP with first term as", first, "and common difference as", cd, "is as follows: \n")
t1, t2, t3, t4 = ap(first,cd)
print(t1, t2, t3, t4)
