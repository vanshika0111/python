# using else with for loop

"""
for loop terminates in two conditions:
        1. it has an exit statement
        2. iterable ends
"""

# CASE 1
list = ["morning", "noon", "evening", "night"]

for item in list:
    print(item)
else:
    print("List ends here")  # displays as the for loop is completely executed

for item in list:
    print(item)
    break
else:
    print("List ends here")  # this won't be displayed as the for loop has a break statement

# CASE 2
list = ["morning", "noon", "evening", "night"]
for item in list:
    if item == "afternoon":
        break
else:
    print("Not found!") 