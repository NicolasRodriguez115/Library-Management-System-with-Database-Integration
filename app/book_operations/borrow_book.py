from database.connect import connect_db
from mysql.connector import Error

def borrow_book():

    try:
        conn = connect_db()
        cursor = conn.cursor()

        book_id = int(input("Enter the id of the book that's being borrowed:\n"))
        status = False # aquí

        update_book = (status, book_id)

        query = "UPDATE books SET status = %s WHERE book_id = %s"

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