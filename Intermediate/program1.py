# library system 
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.borrowed = False

    def borrow_book(self):
        if not self.borrowed:
            self.borrowed = True
            return f"You have borrowed '{self.title} by {self.author}"
        else:
            return f"'{self.title}' is already borrowed"