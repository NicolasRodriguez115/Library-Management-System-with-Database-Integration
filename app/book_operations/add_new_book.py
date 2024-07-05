from app.classes.book import Book
from app.classes.author import authors, Author
from database.connect import connect_db
from mysql.connector import Error
def new_book():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        book_name = input("Enter the title of the book:\n").title().strip()
        author_name = input("Enter the name of the author for the book:\n").title().strip()
        publication_date = input("Enter the publication date of the book:\n").strip()
        status = True
        query = "INSERT INTO books (book_name, author_name, publication_date, status) VALUES (%s, %s,%s, %s)"
        cursor.execute(query, book_name, author_name, publication_date, status) 
        conn.commit()
        input(f"You've succesfully added {book_name} by {author_name} to the library! Press 'enter' to go back.\n ")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

    return


    title = input("Enter the title of the book:\n").title().strip()
    author_name = input("Enter the name of the author for the book:\n").title().strip()
    publication_date = input("Enter the publication date of the book:\n").strip()
    new_book = Book(title, author_name, publication_date, "Available")
    new_book.add_book_to_library()
    for author in authors:
        if author.name == author_name:
            author.add_book(title)
            input(f"You've succesfully added {title} by {author_name} to the library! Press 'enter' to go back.\n ")
            return
        
    print("It appears that this author isn't registered.\nPlease enter the author information so we can add it to the system.")
    nationality = input("What's the nationality of the author?").capitalize().strip()
    new_author = Author(author_name, nationality)
    new_author.new_author()
    new_author.add_book(title)
    input(f"You've succesfully added {title} by {author_name} to the library! Press 'enter' to go back.\n ")
    return
