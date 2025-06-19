class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = int(year)
        

    def __str__(self):
        return "(title) by (author), published in (year)"

    def __rep__(self):
        return f"Book({self.title}, {self.author}, {self.year})"

    def __del__(self):
        print("Deleting (title of the book)")