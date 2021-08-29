# map function

numbers = ["3", "2", "1"]

# numbers[2] = numbers[2] + 1   --> throws an error as strings cannot be added with int

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# numbers[2] = numbers[2] + 1 
# print(numbers[2])

# insted of usinf for loop, use map function
numbers = list(map(int,numbers))
numbers[2] = numbers[2] + 1 
print(numbers[2])

def sq(a):
    return a*a
num = [1,2,3,4,5]
square = list(map(sq,num))
print(square)

num = [1,2,3,4,5]
square = list(map(lambda x:x*x,num))
print(square)

def sqaure(a):
    return a*a
def cube(a):
    return a*a*a
func = [sqaure, cube]
# num = [1,2,3,4,5]
for i in range (5):
    value = list(map(lambda x: x(i), func))
    print(value)