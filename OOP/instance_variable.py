# class variable(s) cannot be changed via instance

"""
print(obj2.salary) --> it will first search if there's a instance of this object
                       if it finds, it will print that value
                       else, it will take the class's value 
"""
class Employee:
    salary = 100
    pass

obj1 = Employee()
obj1.name = "abc"
print("declaring object 1:")
print(obj1.name)
print(obj1.salary)

obj2 = Employee()
print("declaring object 2:")
obj2.name = "xyz"
print(obj2.name)
print(obj2.salary)

print(obj2.__dict__)
obj2.salary = 500
print("creating instance variable")
print(Employee.salary)
print(obj1.salary)
print(obj2.salary)
print(obj2.__dict__)

print(Employee.__dict__)
Employee.salary = 200  
# this will change the property declared in the class
print("manipulating the class property:")
print(Employee.salary)
print(obj1.salary)
print(obj2.salary)
print(Employee.__dict__)

obj2.salary = 200  #instance variable created of the class
print("creating instance variable")
print(Employee.salary)
print(obj1.salary)
print(obj2.salary)


# ALTERNATIVE METHOD TO CHANGE THE VALUE OF VARIABLE(S) --> USING DECORATORS
class Employee:
    salary = 100
    def change_salary(cls, new_salary):
        cls.salary = new_salary

"""
cls is the class for which the instance is created
"""
obj3 = Employee()
print(obj3.salary)
obj3.change_salary(300)
print(obj3.salary)
