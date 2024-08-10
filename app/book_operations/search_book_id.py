from database.connect import connect_db
from mysql.connector import Error
def search_book_id():
    print("""
Books:
------------
""")
    try:
        conn = connect_db()
        cursor = conn.cursor()

        book_id = int(input("Enter the ID of the book you're looking for:\n").strip())
        query = "SELECT book_id FROM books"

        cursor.execute(query)
        for row in cursor.fetchall():
            if row[0] == book_id:
                query = f"SELECT * FROM books WHERE book_id = {book_id}"
                cursor.execute(query)
                for book in cursor.fetchall():
                    print(book)
                    input("Press 'enter' to go back.\n ") 
            else:
                input("That ID doesn't exist. You'll go back to the menu after pressing 'enter'\n ")
                break


    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

    return     