from app.classes.book import library
from app.classes.user import users

def borrow_book():
        title = input("Enter the name of the book:\n").title().strip()
        author = input("Enter the name of the author:\n").title().strip()
        user_id = input(
    """ Enter the ID of the user who will borrow the book 
    (if the user doesn't have a user ID just press 'enter'):\n """).strip()
        for book in library:
            if book.title == title and book.author == author:
                response = book.borrow_book()
                input(response["Message"])
                for user in users:
                    if user.get_user_id() == user_id:
                        user.book_borrowed(book.title)
                        return
                return
        input("The information you entered doesn't match with any book in the library.\nYou'll return to the menu after pressing 'enter'\n ")
        return