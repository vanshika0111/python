# join function

list = ["hii", "hello", "bye", "see", "yaa"]

# METHOD 1
for item in list:
    print(item, " and ", end = " ")
print("others")

# instead of using for loop and another print statement,
# use join function

# METHOD 2
a = " and ".join(list)
a = " , ".join(list)
print(a, "others")