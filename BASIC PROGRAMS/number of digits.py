number = int(input("Enter a number between 0 to 999: "))
if number < 0:
    print("Invalid try! The valid range is 0 to 999.")
elif number < 10:
    print("Single digit number is entered.")
elif number < 100:
    print("Double digit number is entered.")
elif number <= 999:
    print("Three digit number is entered.")
else:
     print("Invalid try! The valid range is 0 to 999.")
