class Book:
## None
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def check_availabality(self):
        if self.available == True:
            print("Книга доступна")
        else:
            print("Книга недоступна")

    def borrow(self):
        if self.available == True:
            print(f"Вы получили книгу {self.title} от {self.author}")
            self.available = False

    def return_book(self):
        if self.available == True:
            print("Книга уже на месте")
        else:
            self.available = True
            print(f"Вы положили книгу {self.title} от {self.author} на место")

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return self.books
        
book1 = Book("Dungeons and dragons", "David", True)
book2 = Book("Harry potter", "Untitled", True)

library1 = Library()

library1.add_book(book1)

print(library1.books)
