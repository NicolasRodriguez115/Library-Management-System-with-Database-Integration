from database.connect import connect_db
from mysql.connector import Error

def new_book():
    while True:
        try:
            conn = connect_db()
            cursor = conn.cursor()

            book_name = input("Enter the title of the book:\n").title().strip()
            author_name = input("Enter the name of the author for the book:\n").title().strip()
            publication_date = input("Enter the publication date of the book:\n").strip()
            status = True

            cursor.execute(f"SELECT author_name, author_nationality FROM authors WHERE author_name like ('%{author_name}%')")
            authors = cursor.fetchall()
            while True:
                if authors:
                    print('These are the authors that we have registered with that name or similar:')

                    for index, author in enumerate(authors):
                        print(f"{index + 1}. {author[0]}")
                    print("If the author is listed above input the number their listed with.\nIf they're not listed input 'x' to register a new author\n").strip()
                    selected_author = input().lower()

                    if selected_author.isdigit():
                        selected_author = int(selected_author) - 1
                        if 0 <= selected_author < len(authors):
                            author = authors[selected_author]
                            query = "INSERT INTO books (book_name, author_name, publication_date, author_id, status) VALUES (%s, %s,%s,%s, %s)"
                            cursor.execute(query, (book_name, author_name, publication_date, author.id, status))
                            conn.commit()
                            input(f"You've successfully added {book_name} by {author_name} to the library! Press 'enter' to go back.\n ")
                            break
                        else:
                            input("You've not entered a valid input. Please try again after pressing enter")
                    elif selected_author == 'x':
                        print('Register a new author:')
                        name = input('Enter the name of the author:\n').title().strip()
                        nationality = input(f'Enter their nationality:\n').capitalize().strip()
                        cursor.execute(f'INSERT INTO authors (author_name, author_nationality) VALUES (%s, %s)', (name, nationality))
                        conn.commit()
                        author_id = cursor.lastrowid
                        input(f"You've successfully registered {name} as an author!\nAfter pressing 'enter' you'll be able to try to add a new book again.\n ")
                        query = "INSERT INTO books (book_name, author_name, publication_date, author_id, status) VALUES (%s, %s,%s,%s, %s)"
                        cursor.execute(query, (book_name, author_name, publication_date, author_id, status))
                        conn.commit()
                        break
                    else:
                        input("You've not entered a valid input. Please try again after pressing enter")
                else:
                    input("There aren't any authors that match that name in our system. You'll create one after pressing enter:\n ")
                    print('Register a new author:')
                    name = input('Enter the name of the author:\n').title().strip()
                    nationality = input(f'Enter their nationality:\n').capitalize().strip()
                    cursor.execute(f'INSERT INTO authors (author_name, author_nationality) VALUES (%s, %s)', (name, nationality))
                    conn.commit()
                    author_id = cursor.lastrowid
                    query = "INSERT INTO books (book_name, author_name, publication_date, author_id, status) VALUES (%s, %s,%s,%s, %s)"
                    cursor.execute(query, (book_name, author_name, publication_date, author_id, status))
                    conn.commit()
                    input(f"You've successfully registered {name} as an author!\nAfter pressing 'enter' you'll be able to try to add a new book again.\n ")
                    break

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

        return