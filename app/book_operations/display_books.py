from database.connect import connect_db
from mysql.connector import Error
def books_display():
    print("""
Books:
---------
          """)
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























    for book in library:
        book.show_book()
    input("When you're done checking the list of books press 'enter'.\n ")
    return