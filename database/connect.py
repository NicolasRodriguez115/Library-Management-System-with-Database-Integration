import mysql.connector
from mysql.connector import Error

def connect_db():
    db_name = "library_management_db"
    user = "root"
    password = "Amoamati1."
    host = "localhost"

    try:
        conn = mysql.connector.connect(
          database=db_name,
          user=user,
          password=password,
          host=host  
        )

        if conn.is_connected():
            print("Connected to MySQL Database succesfully")
            return conn
    except Error as e:
        print(f"Error: {e}")