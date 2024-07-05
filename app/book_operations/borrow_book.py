from database.connect import connect_db
from mysql.connector import Error

def borrow_book():

    try:
        conn = connect_db()
        cursor = conn.cursor()

        book_id = int(input("Enter the id of the book that's being borrowed:\n")).strip()
        status = False

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