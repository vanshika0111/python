# else & finally in try except

# CASE 1: try and excpet
try:
    f = open("does.txt")
except Exception as e:
    print(e)
print("Program ended")

# CASE 2: try, except & finally(must executed)
# no matter try is executed or except, finally is executed for sure
f1 = open("here.txt")
try:
    f2 = open("does.txt")
except Exception as e:
    print(e)
finally:
    print("Run this anyway")
    # f1.close()
    f2.close()
print("Program ended")

# CASE 3: try, except, else
# one is executed from except & else
try:
    f3 = open("does.txt")
except Exception as e:
    print(e)
else:
    print("running as except is not working")
print("Program ended")
