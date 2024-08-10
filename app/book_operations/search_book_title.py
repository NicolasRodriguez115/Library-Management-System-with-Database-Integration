from database.connect import connect_db
from mysql.connector import Error

def search_book_title():
    print("""
Books:
------------
""")
    try:
        conn = connect_db()
        cursor = conn.cursor()

        book_title = input("Enter the title of the book you're looking for:\n").strip().title()
        query = "SELECT book_title FROM books"

        cursor.execute(query)
        for row in cursor.fetchall():
            if row[0] == book_title:
                query = "SELECT * FROM books WHERE book_title = %s"
                cursor.execute(query, (book_title,))
                for book in cursor.fetchall():
                    print(book)
                    input("Press 'enter' to go back.\n ") 

            else:
                input("That title doesn't exist. You'll go back to the menu after pressing 'enter'\n ")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

    return