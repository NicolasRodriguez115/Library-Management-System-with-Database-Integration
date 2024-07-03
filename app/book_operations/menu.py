import os
from app.book_operations import add_new_book as ab, display_books as db, borrow_book as bb,  return_book as rb, search_for_book as sb
def book_operations_menu():
    while True:
        os.system("cls")    
        user_input = input("""
Book Operations:           
    1. Add a new book
    2. Borrow a book
    3. Return a book
    4. Search for a book
    5. Display all books
    6. Quit

""")
        if user_input == "1":
            os.system("cls")
            ab.new_book()
        elif user_input == "2":
            os.system("cls")
            bb.borrow_book()
        elif user_input == "3":
            os.system("cls")
            rb.return_book()
        elif user_input == "4":
            os.system("cls")
            sb.search_book()
        elif user_input == "5":
            os.system("cls")
            db.books_display()
        elif user_input == "6":
            return
        else:
            input("You've not entered a valid option. Please try again after pressing 'enter'\n ")