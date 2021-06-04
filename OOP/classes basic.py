class student:
    
	pass


V = student()

R = student()

# V and R are not assigned to student 
# V and R are objects which are stored into student
#this print statement displays that two objects are created with two different memory allocations
print(V,R)

# the following statements assigns the values to the respective objects
V.name = "abc"

V.std = 11


R.section = "B"
#the following print statement displays the info stored in the object
print(V.name)
print(V.std, R.section)

