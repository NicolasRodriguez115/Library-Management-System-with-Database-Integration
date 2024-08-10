from app.book_operations.menu import book_operations_menu
from app.user_operations.menu import user_operations_menu
from app.author_operations.menu import author_operations_menu
import os
import database.connect as db
from mysql.connector import Error
def main_menu():
    while True:
        os.system("cls")
        db.connect_db()
        user_input = input(
    """
Welcome to the Library Management System!

___  ___  ___  _____ _   _  ___  ___ _____ _   _ _   _ 
|  \/  | / _ \|_   _| \ | | |  \/  ||  ___| \ | | | | |
| .  . |/ /_\ \ | | |  \| | | .  . || |__ |  \| | | | |
| |\/| ||  _  | | | | . ` | | |\/| ||  __|| . ` | | | |
| |  | || | | |_| |_| |\  | | |  | || |___| |\  | |_| |
\_|  |_/\_| |_/\___/\_| \_/ \_|  |_/\____/\_| \_/\___/

    1. Book Operations
    2. User Operations
    3. Author Operations
    5. Quit

    """)
        
        if user_input == "1":
            book_operations_menu()
        elif user_input == "2":
            user_operations_menu()
        elif user_input == "3":
            author_operations_menu()
        elif user_input == "5":
            break
        else:
            input("You've not entered a valid option. Please try again after pressing 'enter'\n ")
