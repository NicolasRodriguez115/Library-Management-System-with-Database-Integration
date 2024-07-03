from app.classes.book import Book
from app.classes.author import authors
def import_books():
    with open("books.txt", "r") as file:
        for line in file:
            title, author, publication_date, status = line.split(';')
            new_book = Book(title, author, publication_date, status)
            new_book.add_book_to_library()
            for author in authors:
                if author.name == author:
                    author.add_book(title)