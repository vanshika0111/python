#this program asks user to enter marks of five subject and calculates the total marks, percentage and shows the pie chart of your result

import matplotlib.pyplot as plt  

print ("-------GRADE CARD-------")
math = int(input("Enter marks of math: "))
physics = int(input("Enter marks of physics: "))
chemistry = int(input("Enter marks of chemistry: "))
english = int(input("Enter marks of english: "))
computer = int(input("Enter marks of computer: "))
total = math + physics + chemistry + english + computer
print("You scored", total, "out of 500.")
percent = (total/500)*100
print("Your percentage is", percent, ",")
print("BEST WISHES YOUR WAY!")
print("Graphical representation of your score: ")
print("\n")
marks = [math, physics, chemistry, english, computer]
subject = ['math','physics','chemistry','english','computer']
plt.axis("equal")
plt.pie(marks, labels = subject, autopct = "%1.1f%%")
plt.show()
print("\n\n")
print("      THANK YOU     ")
