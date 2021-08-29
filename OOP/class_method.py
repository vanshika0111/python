#self is treated as an argument in the definition
"""
print(rohan.PrintDetails())  --> this will replace "self" with "rohan"
"""

class Employee:
    salary = 200
    def PrintDetails(self):
        return f"Name is {self.name}, job is {self.job}."

# creating objects of the class
inked = Employee()
solace= Employee()

# setting the object's properties
inked.name = "Inked"
inked.job = "Teacher"

# setting the object's properties
solace.name = "Solace"
solace.job = "HOD"

print(inked.PrintDetails())
print(solace.PrintDetails())