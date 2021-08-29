# lambda functions or anonymous functions

def add(a,b):
    return a+b

print(add(5,7))

# METHOD 1
lambda_minus = lambda x,y: x-y
print(lambda_minus(6,2))

# METHOD 1
def minus(x,y):
    return x-y

# lambda_minus & minus are equivalent
print(minus(6,12))