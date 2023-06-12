class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author

class Library:
    def __init__(self):
        self.books=[]

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print('Book in the library.')
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}")

    def update_book(self,title,new_author):
        for book in self.books:
            if book.title==title:
                book.author=new_author
                print("Book update succissfully.")
                return
            print("Book not found.")

    def delete_book(self,title):
        for book in self.books:
            if book.title==title:
                self.books.remove(book)
                print("Boook deleted succissfully.")
                return
            print("Book not found.")

def main():
    library = Library()

    while True:
        print("\n=== Library Management System ===")
        print("1. Add a book")
        print("2. Display all books")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Exit")

        choice = input("Enter your choice (1-5) : ")

        if choice=='1':
            title=input("Enter the title of the book: ")
            author=input("Enter the author of the book: ")
            book=Book(title,author)
            library.add_book(book)

        elif choice=='2':
            library.display_books()

        elif choice=='3':
            title=input("Enter the title of the book: ")
            new_author=input("Enter the author of the book: ")
            library.update_book(title, new_author)

        elif choice=='4':
            title=input("Enter the title of the book to deete: ")
            library.delete_book(title)

        elif choice=='5':
            print("Exit the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
