# generators

"""
Iterable: __iter__() or __getitem__()
Iterator:__next__() 
Iteration:
"""

"""
generators are type of iterators
iterable only once
keyword: yield
"""

# CASE 1
def generator(n):
    for i in range (n):
        #return i --> displays 0
        # print(i)  --> displays a loop till range
        yield i  # storage is ready for the range & can be used whenever needed
# METHOD 1
g = generator(7)
print(g)
# METHOD 2
g.__next__()
print(g.__next__())
print(g.__next__())
print(g.__next__())

# for i in range (g):
#     print (i)

# CASE 2
h = "solace"

# METHOD 1
for c in h:
    print (c)
# METHOD 2
ier = iter(h)
print(ier.__next__())
print(ier.__next__())