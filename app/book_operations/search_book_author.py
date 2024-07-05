from database.connect import connect_db
from mysql.connector import Error
def search_book_author():
    print("""
Books:
------------
""")
    try:
        conn = connect_db()
        cursor = conn.cursor()

        book_author = input("Enter the name of the author of the book you're looking for:\n").title.strip()
        query = "SELECT book_author FROM books"

        cursor.execute(query)
        for row in cursor.fetchall():
            if row == book_author:
                query = f"SELECT * FROM books WHERE book_author = {book_author}"
                cursor.execute(query)
                for book in cursor.fetchall():
                    print(book)
                    input("Press 'enter' to go back.\n ") 

            else:
                input("That author doesn't exist. You'll go back to the menu after pressing 'enter'\n ")


    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

    return     