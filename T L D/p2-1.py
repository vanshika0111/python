print("Program by Vanshika Gupta")
Subjects=[] 
for i in range(1,11):
  s1 = input("Enter subject name: ")
  Subjects.insert(i,s1)
print("Dynamic List: ", Subjects)

ElectiveSubjects=["Python", "Advanced Java", "Computer Graphics", "Data Science", "Cyber Security"]
print("Static List: ", ElectiveSubjects)

Subjects.extend(ElectiveSubjects)
print("Extended List: ", Subjects)

Subjects.append("ds")
Subjects.append("C++")
Subjects.append("C")
print("Appended List: ", Subjects)

print("Index of DS: ", Subjects.index("ds"))
print("Index of C++: ", Subjects.index("C++"))
print("Index of C: ", Subjects.index("C"))

value1="ds"
value2="C++"
value3="C"
# value=["ds","C++",C]
try:
  while True:
    Subjects.remove(value1)
    Subjects.remove(value2)
    Subjects.remove(value3)
    # for i in value:
    #   Subjects.remove(i)
except ValueError:
  pass
print("List after removing duplicate elements: ", Subjects)

def remove_range(i1,i2):
  del Subjects[i1:i2]
remove_range(3,7)
print("Resultant List after deleting in range: ", Subjects)

Subjects.reverse()
Subjects.sort()
print("Popping the fifth element: ", Subjects.pop(5))

print("Count of elements in list: ", len(Subjects))

print("Clearing list", Subjects.clear())

print("Program by Vanshika Gupta")

# Which of the above operations can be performed directly?
# Which of the above operations cannot be performed directly on Tuple and why?
# -> Remove and delete operations cannot be performed on tuple as it is immutable.

TupleList = [(1,2), (3.78, 9.56), ("StudyTonight", "Study")]
TupleList.remove((1,2))
print("Removing from tuple list: ", TupleList)
TupleList[0] = 'Vanshika'
print("Updating tuple list: ", TupleList)