from app.classes.user import users
from database.connect import connect_db
from mysql.connector import Error
def display_users():
    print("""
Users:
--------------------
""")
    try:
        conn = connect_db()
        cursor = conn.cursor()

        query = "SELECT * FROM users"

        cursor.execute(query)

        for row in cursor.fetchall():
            print(row) 

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db


