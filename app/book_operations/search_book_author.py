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

        book_author = input("Enter the name of the author of the book you're looking for:\n").title()
        query = f"SELECT * FROM authors where author_name like ('%{book_author}%')"
        cursor.execute(query)
        authors = cursor.fetchall()
        for index, author in enumerate(authors):
            print(str(index + 1) + ' ' + author[1])
        selectedAuthor = input('select the number of the author')
        cursor.execute(f"Select * from books where author_id = {authors[int(selectedAuthor) - 1][0]}")
        books = cursor.fetchall()
        for book in books:
            print(book)

        else:
            print("That author doesn't exist. You'll go back to the menu after pressing 'enter'\n")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

    return