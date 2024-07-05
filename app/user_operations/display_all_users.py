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

        input("Press 'enter' to go back.\n ")      

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
    
    return


