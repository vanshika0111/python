class Employee:
    salary = 100
    _protec = 200
    __private = 300

obj = Employee()
print(obj.salary)
print(obj._protec)
# print(obj.__private)   --> private cannot be accessed directly
print(obj._Employee__private)