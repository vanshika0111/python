"""
flow of execution:
    first it searches for a instance in B class
    if not present, it will search in the class inheritted

once a def is overridden, it cannot be executed again
however, super() can be used to call the first class of inheritance
"""


class A:
    class_var1 = "I am in class A"
    def __init__(self):
        self.var1 = "I am in class A's constructor"
        self.class_var1 = "Instance of class A"
        self.special = "Special"

class B(A):
    var2 = "I am in class B"
    def __init__(self):
        super().__init__()
        # print(super().special)
        self.var1 = "I am in class B's constructor"
        self.class_var1 = "Instance of class b"

a = A()
b = B()

print(b.class_var1)
        