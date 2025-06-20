class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    super().__init__(self, file_size):
        self.file_size = int(file_size)

class PrintBook(Book):
    super().__init__(self, page_count):
        self.page_count = int(page_count)

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Only Book instances can be added.")


    def list_books(self):
        found = False
        for book in self._books:
            if book.is_available():
                print(f" - {book}")
                found = True
        if not found:
            print("No books available.")


        