YearAge = int(input("Enter you age or birth year: "))

isAge = False
isYear = False

if len(str(YearAge)) == 4:
    isYear = True
else:
    isAge = True
# else:
#     print("There was some problem.")
#     exit()

if (YearAge < 1900 and isYear):
    print("Wow! You seem to be one of the oldest person alive.")
    exit()
if YearAge > 2021:
    print("You sure you are born yet?")
    exit()

if isAge:
    YearAge = 2021 - YearAge

print(f"You will be of 100 years in {YearAge + 100}")

Year = int(input("Enter the year you want to know age in: "))
print(f"You will be {Year-YearAge} years old in {Year}")

age = input("Thank you")
