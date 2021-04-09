#this program is of a letter template. Just enter the name and date and it will generate a letter for you.

letter = '''Dear <|NAME|>,
Greetings! 
You are selected!
Have a great day ahead.
Thanks for joining us.

Date: <|DATE|>
'''
name = input("Enter reciever's name: ")
date = input("\nEnter date: ")
print("\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)