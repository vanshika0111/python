# f-string or string formatting

first_name = "solace"
name = "inked"

# METHOD 1
print("This is %s" %first_name)

# METHOD 2
print("This is " + first_name)

# METHOD 3
a = "It's a good {}"
b = a.format(first_name)
print(b)
c = "It's a good {1} {0}"
d = c.format(first_name, name)
print(d)

# METHOD 4
final = f"This is finally me, {name} {first_name}"
print(final)
