class Library:
    def __init__(self, list_of_books, Lname): #constructor
        
        #library name
        

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        
            
    
    def addBook(self, book):
        
        print(f"{book} has been added to the book list.")

    def lendBook(self, user, book):
        if :
            print("Sorry, we do not have that book.")
        elif :
            print(f"The book is already being used by {self.lendDict[book]}")
        else:
            
            print("Lender-Book database has been updated. You can take the book now.")

    def returnBook(self, book):
        
            
            print("Book has been returned.")
        else:
            print("That book wasn't borrowed from us.")


if __name__ == '__main__':
    books = Library(
        ['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], 
        "Let's Upskill")

    user_name = input("Welcome to our library! Please enter your name: ")

    while True:
        print(f"Hello {user_name}, welcome to the {books.name} library. Please choose an option:")

        print("1. Display Books\n2. Lend a Book\n3. Add a Book\n4. Return a Book\n5. Quit")
        
        user_choice = 

        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Please enter a valid option.")
            continue

        if user_choice == '1':
            books.displayBooks()
        elif user_choice == '2':
            book = input()
            books.lendBook(user_name, book)
        elif user_choice == '3':
            book = input()
            books.addBook(book)
        elif user_choice == '4':
            book = input()
            books.returnBook(book)
        elif user_choice == '5':
            print(f"Thank you for using the library, {user_name}. Goodbye!")
            break
