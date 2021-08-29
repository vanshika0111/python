# decorators

# CASE 1
def function1():
    print("hello")

function2 = function1
del function1   #deletes function1
function2()

# CASE 2
def return_func(num):
    if num==0:
        return print
    if num==1:
        return int
        # return sum
a = return_func(1)
print(a)
b = return_func(0)
print(b)

# CASE 3
def executor(func):
    func("bye")

executor(print)

# CASE 4
def decorator(func1):
    def now_execute():
        print("Executing now")
        func1()
        print("Executed")
    return now_execute

# METHOD 1
def who():
    print("good")

who()
who = decorator(who)
who()

# METHOD 2
@decorator
def who():
    print("good")
who()