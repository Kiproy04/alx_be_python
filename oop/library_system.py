class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def add_book(self):
        self.title.author.add_book()

    def list_books(self):
        self.title.author.list_books()

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)

        def __str__(self):
            super().__init__(title, author)
            return f"EBook: {self.title} by {self.author} File Size: {self.file_size}"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)

        def __str__(self):
            super().__init__(title, author)
            return f"PrintBook: {self.title} by {self.author} Page Count: {self.page_count}"


class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book instances can be added.")


    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in the library:")
        for book in self.books:
            print(f"{book}")
        


        