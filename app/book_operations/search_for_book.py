from app.classes.book import library
def search_book():
    title = input("Enter the title of the book:\n").title()
    print("---------")
    for book in library:
        if book.title == title:         
            book.show_book()
            input("Press 'enter' to go back.\n ")
