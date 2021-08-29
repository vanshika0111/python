try:
    a = int(input("Enter any number: "))
    b = 1/a
except Exception as e:
    print(e)
    //exit()
finally:
    print("Done")
print("Thanks")