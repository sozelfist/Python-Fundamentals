

class Book:
    def __init__(self, title: str, author: str, ISBN: str):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.borrowed = False

    def borrow(self):
        if self.borrowed:
            print(
                f"Sorry, the book {self.title} by {self.author}\
                     is already borrowed.")
        else:
            self.borrowed = True
            print(
                f"You have successfully borrowed\
                     {self.title} by {self.author}.")

    def return_book(self):
        if not self.borrowed:
            print(
                f"Sorry, the book {self.title}\
                     by {self.author} is not on loan.")
        else:
            self.borrowed = False
            print(f"Thank you for returning {self.title} by {self.author}.")


class Library:
    def __init__(self, name: str, books: list[Book]):
        self.name = name
        self.books = books

    def search(self, title: str) -> Book | None:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} - ISBN: {book.ISBN}")


if __name__ == '__main__':
    book1 = Book("Pride and Prejudice", "Jane Austen", "978-0345806565")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0446310789")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273567")

    books = [book1, book2, book3]

    library = Library("Main Library", books)

    library.display_books()

    book = library.search("The Great Gatsby")

    if book:
        book.borrow()
    else:
        print("The book is not available in the library.")
