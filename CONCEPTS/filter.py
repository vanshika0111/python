# filter function

list1 = [1,2,3,4,5,6,7,8,9,10]

# METHOD 1
def is_greater(num):
    return num>5

# METHOD 2
greater_than_5 = filter(is_greater,list1)
print(greater_than_5)
greater_than_5 = list(filter(is_greater,list1))
print(greater_than_5)