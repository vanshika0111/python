# constructors can be used alternatively instead of class method

# alternative constructor takes one argument and splits it 
class Employee:
    def from_str(cls,string):
        inked = string.split("-")
        return cls(inked[0], inked[1])
        # return cls(*string.split("-"))

solace = Employee.from_str("solace-teacher")
print(solace.name)