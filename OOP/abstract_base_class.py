# abstract base class & abstract method

"""
abstract class specifies that all the further should have the respective class method
abstract base class cannot have any object
"""

from abc import ABCMeta, abstractmethod
# from abc import ABC, abstractmethod --> for version 3.4 & above

# class Shape(ABC) --> for version 3.4 & above
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 8

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
# it will throw an error if def printarea is not dclared in rectangle class

print(rect1.printarea())