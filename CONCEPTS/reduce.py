# reduce function

from functools import reduce

list = [1,2,3,4]

# METHOD 1
num = 0
for i in list:
    num = num + i
print(num)

# METHOD 2
num = reduce(lambda x,y: x+y, list)
print(num)