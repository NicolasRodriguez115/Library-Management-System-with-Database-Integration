from database.connect import connect_db
from mysql.connector import Error
def return_book():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        book_id = int(input("Enter the id of the book that's being returned:\n")).strip()
        status = True

        update_book = (status, book_id)

        query = "UPDATE books SET status = %s WHERE customer_id = %s"

        cursor.execute(query, update_book)
        conn.commit()
        input("Book status changed succesfully updated! Press 'enter' to go back.\n ")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close() 

    return

        # while True:
        #     title = input("Enter the name of the book:\n").title().strip()
        #     author = input("Enter the name of the author:\n").title().strip()
        #     user_id = input(
        # """ Enter the ID of the user who borrowed the book 
        # (if the user doesn't have a user ID just press 'enter'):\n """).strip()
        #     for book in library:
        #         if book.title == title and book.author == author:
        #             response = book.return_book()
        #             print(response["Message"])
        #             for user in users:
        #                 if user.get_user_id() == user_id:
        #                     user.book_returned(book.title)
        #                     return
        #                 else:
        #                     return
        #         else:
        #             try_or_exit = input(
        # """That information doesn't match any book in the library 
        # (make sure that you spelled the title and name of the author correctly). 
        # If you want to try again enter 'yes'. If you want to go exit enter 'no'.\n""").lower()
        #             if try_or_exit == "yes":
        #                 input("You'll be able to try again after pressing 'enter'\n ")
        #             elif try_or_exit == "no":
        #                 return
        #             else:
        #                 input("You didn't enter a valid option. You'll return to the menu after pressing 'enter'.\n ")
        #                 return
                    