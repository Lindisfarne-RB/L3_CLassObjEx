import os
'''class Library:

    def __init__(self):
        pass
    def display(self ):
        pass
    class Student:
        pass






class Library:

    def __init__(self, liostofBooks):
        self.books = liostofBooks

    def displayAvailableBooks(self):
        print("Books present in this libarary are")
        for book in self.books:
            print(" " +book)

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.Please keep it safe")
            self.books.remove(bookName)
        else:
            print("Sorry, this book is already issued to someone else")

    def returnBooks(self, bookName):
        self.books.append(bookName)
        print("Thank you for retuning this book")



class Student:
    pass


if __name__ == "__main__":
    centralLibrary = Library (["Algorithms in Py" , "Py Framework Django", "Py website Flask", "AI with Py" , "Data Sc with Py"])
    centralLibrary.displayAvailableBooks()



class Library:

    def __init__(self, liostofBooks):
        self.books = liostofBooks

    def displayAvailableBooks(self):
        print("Books present in this libarary are")
        for book in self.books:
            print(" " + book)

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.Please keep it safe")
            self.books.remove(bookName)
        else:
            print("Sorry, this book is already issued to someone else")

    def returnBooks(self, bookName):
        self.books.append(bookName)
        print("Thank you for retuning this book")


class Student:
    def requestBook(self):
        self.book = input ("Enter the name of the book you want to borrow")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(
        ["Algorithms in Py", "Py Framework Django", "Py website Flask", "AI with Py", "Data Sc with Py"])
    centralLibrary.displayAvailableBooks()
'''



class Library:

    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print("Books present in this libarary are")
        for book in self.books:
            print(" " + book)

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.Please keep it safe")
            self.books.remove(bookName)
        else:
            print("Sorry, this book is already issued to someone else")

    def returnBooks(self, bookName):
        self.books.append(bookName)
        print("Thank you for retuning this book")


class Student:
    def requestBook(self):
        self.book = input ("Enter the name of the book you want to borrow")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return")
        return self.book



def clear_screen():
        print('\n' * 25)

if __name__ == "__main__":
    clear_screen()
    centralLibrary = Library(
        ["Algorithms in Py", "Py Framework Django", "Py website Flask", "AI with Py", "Data Sc with Py"])
    #centralLibrary.displayAvailableBooks()
    student = Student()
    while (True):
        welcomeMsg = '''++++Welcome to Central Library +++++
        Please choose an option
        1 List all books
        2 Request a book
        3 Return a book
        4 Exit the program
         '''

        print(welcomeMsg)
        a = int( input("Enter a choice  - "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:

            centralLibrary.borrowBooks(student.requestBook())
        elif a == 3:
            centralLibrary.returnBooks(student.returnBook())

        elif a==4: exit()

        else:
            print("Invalid choice")


