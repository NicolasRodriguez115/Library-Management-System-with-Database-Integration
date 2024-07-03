import os
from app.user_operations.add_new_user import new_user
from app.user_operations.view_user_details import user_details
from app.user_operations.display_all_users import display_users
def user_operations_menu():
    while True:
        os.system("cls")
        user_input = input("""
User Operations:                          
    1. Add a new user
    2. View user details
    3. Display all users
    4. Quit
                                                  
""")
        if user_input == "1":
            os.system("cls")
            new_user()
        elif user_input == "2":
           os.system("cls")
           user_details()
        elif user_input == "3":
            os.system("cls")
            display_users()
        elif user_input == "4":
            return
        else:
            input("You've not entered a valid option. Please try again after pressing 'enter'\n ")