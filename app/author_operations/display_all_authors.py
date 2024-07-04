from database.connect import connect_db
from mysql.connector import Error
def display_authors():
    print("""
Authors:
------------
""")
    try:
        conn = connect_db()
        cursor = conn.cursor()

        query = "SELECT * FROM authors"

        cursor.execute(query)

        for row in cursor.fetchall():
            print(row) 

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()     