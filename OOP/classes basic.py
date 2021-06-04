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
#the following print statement illustrates displaying both object's info
print(V.std, R.section)
#the following statement will throw an error as R's name is not declared
#print(R.name)
# list can also be added as values
R.language = ["hindi","english"]
print(R.language)

