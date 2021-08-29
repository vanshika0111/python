# creating constructor
"""
synatx of constructor:
    def __init__(self, arg1, arg2):
        pass

here, self --> object name
      arg1 --> argument one
      arg2 --> argument two

__init__ self-initialises the constructor
"""

class Employee:
    salary = 200
    def __init__(self, obj_name, obj_job):
        self.name = obj_name
        self.job = obj_job

inked = Employee("Inked", "Teacher")
print(inked.job)
# print(inked.Employee) --> throws an error