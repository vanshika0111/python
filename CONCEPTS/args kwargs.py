# *args & **kwargs 

def function_name_print(a,b,c,d):
    print(a,b,c,d)

function_name_print("hii", "hello", "bye", "see")
# function_name_print("hii", "hello", "bye", "see", "yaa") --> throws an error as function accepts only 4 args

# METHOD 1
def func_args(*args):
    print(type(args))
    # print(normal)
    print(args[0])   #displays zero index
    for item in args:
        print(item)

# METHOD 2
# def func_args(*args,normal):  --> throws an error; *arg is always in last
def func_args(normal, *args):
    # print(type(args))
    print(normal)
    print(args[0])   #displays zero index
    for item in args:
        print(item)

normal = "It can have any name inspite of normal"
a = ["hii", "hello", "bye", "see", "yaa"]
print(a)
func_args(*a)
func_args(normal,*a)
# func_args(*a, normal) --> throws an error; *arg is always in last

# METHOD 3
kwarg = {"inked: first", "solace:last"}
# following both def are equivalent
# def func_args(normal, *args, **kwargs):
def func_args(*args,normal,**kwargs):
    for key,value in kwarg.items():
        print(key,value)