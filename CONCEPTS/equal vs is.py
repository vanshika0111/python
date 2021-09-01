"""
== --> value equality     --> two objects have same value
is --> reference equality --> two references refer to the same object

Example:
    two different objects have same value --> ==
    two references have same value        --> is
"""

a = [1,2,3]
b = a 
print( b == a)   # true
print( a == b)   # true
print( b is a)   # true
print( a is b)   # true
b[0] = 0
print(b)
print(a) 
c = a[:]
print(c)
print( b == c )   # true
print( a == c)   # true
print( c is a)   # false
