class Book:
    def __init__(self, title, author):
        self.title = title                # public
        self.author = author              # public
        self._is_checked_out = False      # private

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"'{self.title}' by {self.author}"

        
class Library:
    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Only Book instances can be added.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"You checked out: {book}")
                return
        print(f"Book '{title}' is not available or doesn't exist.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"You returned: {book}")
                return
        print(f"Book '{title}' is not checked out or doesn't exist.")

    def list_available_books(self):
        print("Available books:")
        found = False
        for book in self._books:
            if book.is_available():
                print(f" - {book}")
                found = True
        if not found:
            print("No books available.")
