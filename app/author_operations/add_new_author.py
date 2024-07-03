from app.classes.author import Author
def new_author():
    name = input("Enter the first and last name of the author:\n").title().strip()
    nationality = input("Enter the nationality of the athor:\n").capitalize().strip()
    new_author = Author(name, nationality)
    new_author.new_author()
    input(f"You've succesfully added {name} as an author to the library! Press 'enter' to go back.\n ")
    return

