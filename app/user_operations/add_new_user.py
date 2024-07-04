from database.connect import connect_db
from mysql.connector import Error
import random 
def new_user():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        name = input("Enter the first and last name of the user:\n").title().strip()
        query = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(query, name) # prepares query with arguments
        conn.commit()
        input(f"You've succesfully created a user for {name} with customer ID {user_id} to the library! Press 'enter' to go back.\n ")
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
    return
    