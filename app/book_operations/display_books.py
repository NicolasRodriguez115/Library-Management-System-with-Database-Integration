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

        query = """
        SELECT b.book_id, b.book_name, a.author_name, b.publication_date, b.status
        FROM books b
        JOIN authors a ON b.author_id = a.author_id
        """

        cursor.execute(query)

        for row in cursor.fetchall():
            book_id, book_name, author_name, publication_date, status = row
            status_str = "available" if status else "borrowed"
            print(f"Book ID: {book_id}, Book Name: {book_name}, Author: {author_name}, Year: {publication_date}, Status: {status_str}")

        input("Press 'enter' to go back.\n ") 

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()