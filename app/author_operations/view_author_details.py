from app.classes.author import authors
import os
def author_details():
    select_author = input("Enter the first and last name of the author you're looking for:\n").title().strip()
    os.system('cls')
    for author in authors:
        if author.name == select_author:
            author.author_details()
            input("Press 'enter' to go back.\n ")
            return
        else:
            input("That author is not registered in the library yet. You'll return to the menu after pressing 'enter'.\n ")
            return

