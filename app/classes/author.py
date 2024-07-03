authors = []
class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
    
    def new_author(self):
        authors.append(self)

    def add_book(self, book):
        self.books.append(book)

    def show_author(self):
        print(f"Name: {self.name}\n-------")
    
    def list_of_books(self):
        for book in self.books:
            print(book)

    def author_details(self):
        print(f"{self.name} ~ {self.nationality}\nWe currently own the following books by this author:")
        self.list_of_books()