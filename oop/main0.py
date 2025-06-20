from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)
    my_book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    # Demonstrating the __str__ method
    print(my_book)
    print(my_book2)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))
    print(repr(my_book2))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()