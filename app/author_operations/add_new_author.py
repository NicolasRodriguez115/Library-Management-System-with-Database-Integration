from database.connect import connect_db
from mysql.connector import Error
def new_author():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        author_name = input("Enter the first and last name of the author:\n").title().strip()
        author_nationality = input("Enter the nationality of the author:\n").capitalize().strip()
        query = "INSERT INTO authors (author_name, author_nationality) VALUES (%s, %s)"
        cursor.execute(query, author_name, author_nationality) 
        conn.commit()
        input(f"You've succesfully added {author_name} as an author to the library! Press 'enter' to go back.\n ")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

    return

