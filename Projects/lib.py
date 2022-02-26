class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.IssueDictionary = {}

    def DisplayBooks(self):
        print(f"Welcome to {self.name} e-Library.")
        print("We have the following books: ")
        for book in self.booklist:
            print(book)

    def IssueBook(self, user, book):
        if book not in self.IssueDictionary.keys():
            self.IssueDictionary.update({book:user})
            print("Data is added in the database. Enjoy reading.")
        else:
            print(f"This book is already issued by {self.IssueDictionary[book]}.")

    def AddBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the list.")

    def ReturnBook(self,book):
        self.IssueBook.pop(book)

if __name__ == '__main__':
    object = Library(['Python', 'OOP', 'C++', 'C', 'Data Structure', 'DataBase Managemnet System' ], "Online")
    while (True):
        print(f"Welcome to {object.name} library.")
        print("Choices availabe are: ")
        print("1. Display book")
        print("2. Issue book")
        print("3. Add book")
        print("4. Return book")
        print("Enter appropriate choice: ")
        choice = int (input ())

        if choice == 1:
            object.DisplayBooks()
        elif choice == 2:
            book = input("Enter the title of book: ")
            user = input ("Enter your name: ")
            object.IssueBook(user,book)
        elif choice == 3:
            book = input("Enter the title of book you want to add: ")
            object.AddBook(book)
        elif choice == 4:
            book = input("Enter the title of book you want to return: ")
            object.ReturnBook(book)
        else:
            print("Invalid option")

        print("Press q to quit or c to continue.")
        choice2 = ' '
        while (choice2 != "c" and "q"):
            choice2 = (input())
            if choice2 == "q" or "Q":
                exit()
            elif choice2 == "c" or "C":
                continue

