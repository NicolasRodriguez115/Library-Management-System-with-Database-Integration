from database.connect import connect_db
from mysql.connector import Error
from app.book_operations.search_book_id import search_book_id
import os
def search_book():
    while True:    
        user_input = input("""
Please select the option by which you'd like to search for a book.           
    1. Book ID
    2. Book Title
    3. Author
    4. Quit
""")
        if user_input == "1":
            os.system("cls")
            search_book_id()
        elif user_input == "2":
            os.system("cls")
            borrow_book()
        elif user_input == "3":
            os.system("cls")
            return_book()
        elif user_input == "4":
            return
        else:
            input("You've not entered a valid option. Please try again after pressing 'enter'\n ")
    try:
        conn = connect_db()
        cursor = conn.cursor()


        query = "SELECT * FROM books"

        cursor.execute(query)

        for row in cursor.fetchall():
            print(row) 

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()     



























    title = input("Enter the title of the book:\n").title()
    print("---------")
    for book in library:
        if book.title == title:         
            book.show_book()
            input("Press 'enter' to go back.\n ")
