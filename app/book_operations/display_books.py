from app.classes.book import library
def books_display():
    print("""
Books:
---------
          """)
    for book in library:
        book.show_book()
    input("When you're done checking the list of books press 'enter'.\n ")
    return