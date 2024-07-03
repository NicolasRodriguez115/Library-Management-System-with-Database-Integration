from app.mock_library.import_authors import import_authors
from app.mock_library.import_books import import_books
from app.mock_library.import_users import import_users
def import_library():
    import_authors()
    import_books()
    import_users()
    input("You've succesfully imported a library!\nYou'll return to the main menu after pressing 'enter'.\n ")
    