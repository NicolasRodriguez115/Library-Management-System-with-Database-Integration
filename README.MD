# `main_menu.py`  Documentation

## Overview

This script is the main menu for the Library Management System. It provides options for navigating to different operations within the system, such as book operations, user operations, and author operations. The menu is displayed in a loop until the user chooses to quit.

## Imports

-   `from app.book_operations.menu import book_operations_menu`: Imports the function to handle book operations.
-   `from app.user_operations.menu import user_operations_menu`: Imports the function to handle user operations.
-   `from app.author_operations.menu import author_operations_menu`: Imports the function to handle author operations.
-   `import os`: Provides a way to interact with the operating system.
-   `import database.connect as db`: Imports the database connection module.
-   `from mysql.connector import Error`: Imports the error handling for MySQL connector.

## Functions

### `main_menu()`

This function displays the main menu and handles user input to navigate to different sections of the Library Management System.

#### Functionality

1.  **Clear Screen**: Clears the terminal screen using  `os.system("cls")`.
2.  **Database Connection**: Connects to the database using  `db.connect_db()`.
3.  **Display Menu**: Displays the main menu with options for different operations.
4.  **User Input**: Waits for the user to input a choice.
5.  **Menu Navigation**:
    -   If the user inputs "1", it calls  `book_operations_menu()`.
    -   If the user inputs "2", it calls  `user_operations_menu()`.
    -   If the user inputs "3", it calls  `author_operations_menu()`.
    -   If the user inputs "5", it breaks the loop and exits the menu.
    -   For any other input, it prompts the user to try again.

#### Example

def  main_menu():

while  True:

os.system("cls")

db.connect_db()

user_input  =  input(

"""

Welcome to the Library Management System!

___ ___ ___ _____ _ _ ___ ___ _____ _ _ _ _

| \/ | / _ \|_ _| \ | | | \/ || ___| \ | | | | |

| . . |/ /_\ \ | | | \| | | . . || |__ | \| | | | |

| |\/| || _ | | | | . ` | | |\/| || __|| . ` | | | |

| | | || | | |_| |_| |\ | | | | || |___| |\ | |_| |

\_| |_/\_| |_/\___/\_| \_/ \_| |_/\____/\_| \_/\___/

1. Book Operations

2. User Operations

3. Author Operations

5. Quit

""")

if  user_input  ==  "1":

book_operations_menu()

elif  user_input  ==  "2":

user_operations_menu()

elif  user_input  ==  "3":

author_operations_menu()

elif  user_input  ==  "5":

break

else:

input("You've not entered a valid option. Please try again after pressing 'enter'\n ")

## Usage

To use this script, simply call the  `main_menu()`  function. This will start the main menu loop and allow the user to navigate through the different operations of the Library Management System.

if  __name__  ==  "__main__":

main_menu()

## Notes

-   Ensure that the database connection details are correctly configured in the  `database.connect`  module.
-   The script uses  `os.system("cls")`  to clear the screen, which is specific to Windows. For cross-platform compatibility, consider using a different method to clear the screen.

# `menu.py`  Documentation

## Overview

The  `menu.py`  script provides a command-line interface for managing book operations. It allows users to add, borrow, return, search for, and display books. The script continuously prompts the user for input until they choose to quit.

## Functions

### `book_operations_menu()`

This function displays a menu with various book operations and executes the corresponding function based on user input.

#### Menu Options:

1.  **Add a new book**: Calls  `ab.new_book()`  to add a new book.
2.  **Borrow a book**: Calls  `bb.borrow_book()`  to borrow a book.
3.  **Return a book**: Calls  `rb.return_book()`  to return a borrowed book.
4.  **Search for a book**: Calls  `sb.search_book()`  to search for a book.
5.  **Display all books**: Calls  `db.books_display()`  to display all books.
6.  **Quit**: Exits the menu.

#### Implementation Details:

-   The menu is displayed in a loop, clearing the screen (`os.system("cls")`) before each prompt.
-   User input is read and stripped of leading/trailing whitespace.
-   Based on the input, the corresponding function from  `app.book_operations`  is called.
-   If the input is invalid, an error message is displayed, and the user is prompted to try again.

## Usage

To use this script, simply run it in a Python environment. The menu will appear, and you can interact with it by entering the corresponding number for each operation.

## Dependencies

-   `os`: Used to clear the screen.
-   `app.book_operations`: Module containing the book operation functions (`add_new_book`,  `display_books`,  `borrow_book`,  `return_book`,  `search_for_book_menu`).

## Example

import  os

from app.book_operations import add_new_book as ab, display_books as db, borrow_book as bb, return_book as rb, search_for_book_menu as sb

def  book_operations_menu():

while  True:

os.system("cls")

user_input  =  input("""

Book Operations:

1. Add a new book

2. Borrow a book

3. Return a book

4. Search for a book

5. Display all books

6. Quit

""").strip()

if  user_input  ==  "1":

os.system("cls")

ab.new_book()

elif  user_input  ==  "2":

os.system("cls")

bb.borrow_book()

elif  user_input  ==  "3":

os.system("cls")

rb.return_book()

elif  user_input  ==  "4":

os.system("cls")

sb.search_book()

elif  user_input  ==  "5":

os.system("cls")

db.books_display()

elif  user_input  ==  "6":

return

else:

input("You've not entered a valid option. Please try again after pressing 'enter'\n ")

# `add_new_book.py`  Documentation

## Overview

This script allows users to add new books to a library database. It interacts with a MySQL database to check for existing authors and register new authors if necessary.

## Functions

### `new_book()`

This function handles the process of adding a new book to the library database. It performs the following steps:

1.  Connects to the database.
2.  Prompts the user to enter the book's title, author's name, and publication date.
3.  Checks if the author already exists in the database.
4.  If the author exists, it allows the user to select the author from a list.
5.  If the author does not exist, it prompts the user to register a new author.
6.  Inserts the new book into the database.
7.  Handles any database connection errors.
8.  Closes the database connection.

## Detailed Steps

1.  **Database Connection**:
    
    -   Establishes a connection to the database using  `connect_db()`.
    -   Creates a cursor for executing SQL queries.
2.  **User Input**:
    
    -   Prompts the user to enter the book's title, author's name, and publication date.
    -   Strips and formats the input values.
3.  **Author Check**:
    
    -   Executes a SQL query to check if the author exists in the database.
    -   Fetches the results and displays a list of matching authors.
4.  **Author Selection**:
    
    -   If matching authors are found, the user can select an author from the list or choose to register a new author.
    -   If no matching authors are found, the user is prompted to register a new author.
5.  **Register New Author**:
    
    -   Prompts the user to enter the new author's name and nationality.
    -   Inserts the new author into the database and retrieves the new author's ID.
6.  **Insert New Book**:
    
    -   Inserts the new book into the database with the provided details and the author's ID.
    -   Commits the transaction to save the changes.
7.  **Error Handling**:
    
    -   Catches and prints any database connection errors.
8.  **Close Connection**:
    
    -   Closes the cursor and the database connection.

## Example Usage

To use this script, simply call the  `new_book()`  function. The function will guide you through the process of adding a new book to the library database.

from add_new_book import new_book

new_book()

## Dependencies

-   `mysql.connector`: Used for connecting to and interacting with the MySQL database.
-   `connect_db`: A function from  `database.connect`  module that establishes a database connection.

## Notes

-   Ensure that the database connection details are correctly configured in the  `connect_db`  function.
-   The script assumes that the  `authors`  and  `books`  tables exist in the database with the appropriate schema.

## Error Handling

-   The script handles database connection errors and prints the error message.
-   It ensures that the database connection is closed properly even if an error occurs.

# `borrow_book.py`

## Overview

This script is responsible for updating the status of a book in the database to indicate that it has been borrowed. It connects to a MySQL database, updates the status of the specified book, and handles any potential errors during the process.

## Functions

### `borrow_book()`

This function prompts the user for the ID of the book being borrowed, updates the book's status in the database, and handles any errors that may occur.

#### Workflow:

1.  Connect to the database using  `connect_db()`.
2.  Create a cursor object to interact with the database.
3.  Prompt the user to enter the ID of the book being borrowed.
4.  Set the status of the book to  `False`  (indicating it is borrowed).
5.  Prepare the SQL query to update the book's status.
6.  Execute the SQL query with the provided book ID and status.
7.  Commit the transaction to save the changes.
8.  Prompt the user to press 'enter' to go back.
9.  Handle any database connection errors.
10.  Ensure the database connection is closed properly.

#### Example Usage:

borrow_book()

## Dependencies

-   `database.connect.connect_db`: A function to establish a connection to the database.
-   `mysql.connector.Error`: An exception class for handling MySQL errors.

## Error Handling

The function catches and prints any  `mysql.connector.Error`  that occurs during the database operations.

## Cleanup

The function ensures that the database connection is closed properly in the  `finally`  block, even if an error occurs.

## Notes

-   The status of the book is hardcoded to  `False`  to indicate that the book is borrowed.
-   The user is prompted to enter the book ID via the console.
-   Ensure that the  `connect_db`  function is correctly implemented and available in the  `database.connect`  module.

# `return_book.py`

## Overview

This script is responsible for updating the status of a book in the database to indicate that it has been returned. It connects to the database, updates the book's status, and handles any potential errors during the process.

## Functions

### `return_book()`

This function updates the status of a book in the database to indicate it has been returned.

#### Workflow:

1.  Connect to the database using  `connect_db()`.
2.  Create a cursor object to execute SQL queries.
3.  Prompt the user to enter the ID of the book being returned.
4.  Set the status of the book to  `True`  (indicating it is returned).
5.  Prepare the SQL query to update the book's status.
6.  Execute the SQL query with the provided book ID and status.
7.  Commit the transaction to save changes to the database.
8.  Prompt the user to press 'enter' to go back after the status is successfully updated.
9.  Handle any potential database errors.
10.  Ensure the database connection is closed properly in the  `finally`  block.

#### Exception Handling:

-   Catches and prints any  `mysql.connector.Error`  that occurs during the database operations.

#### Database Operations:

-   Connects to the database.
-   Executes an  `UPDATE`  SQL query to change the book's status.
-   Commits the transaction to save changes.

## Example Usage

To use this script, simply run it and follow the prompts to enter the ID of the book being returned. The script will handle the rest, updating the book's status in the database.

if  __name__  ==  "__main__":

return_book()

## Dependencies

-   `mysql.connector`: Used for connecting to and interacting with the MySQL database.
-   `database.connect`: Custom module for establishing a database connection.

## Error Handling

-   The script handles  `mysql.connector.Error`  exceptions and prints an error message if an exception occurs during the database operations.

## Notes

-   Ensure that the  `database.connect`  module is correctly implemented and accessible.
-   The script assumes that the  `books`  table in the database has a  `status`  column and a  `book_id`  column.

# `search_for_book_menu.py`

## Overview

This script provides a menu-driven interface for searching books in a database. Users can search for books by ID, title, or author. The script interacts with the database and performs the search operations based on user input.

## Dependencies

-   `mysql.connector`: Used for handling MySQL database connections and operations.
-   `os`: Used for clearing the console screen.
-   `database.connect.connect_db`: Custom module for connecting to the database.
-   `app.book_operations.search_book_id`: Custom module for searching books by ID.
-   `app.book_operations.search_book_title`: Custom module for searching books by title.
-   `app.book_operations.search_book_author`: Custom module for searching books by author.

## Functions

### `search_book()`

This function displays a menu to the user and prompts them to select an option for searching a book. The options include searching by book ID, title, author, or quitting the menu.

#### Menu Options:

1.  **Book ID**: Clears the console and calls the  `search_book_id()`  function.
2.  **Book Title**: Clears the console and calls the  `search_book_title()`  function.
3.  **Author**: Clears the console and calls the  `search_book_author()`  function.
4.  **Quit**: Exits the menu.

If the user enters an invalid option, they are prompted to try again.

## Usage

To use this script, simply run it in a Python environment. The script will display a menu and prompt the user to select an option for searching a book.

if  __name__  ==  "__main__":

search_book()

## Example

Please select the option by which you'd like to search for a book.

1. Book  ID

2. Book Title

3. Author

4. Quit

-   Enter  `1`  to search by Book ID.
-   Enter  `2`  to search by Book Title.
-   Enter  `3`  to search by Author.
-   Enter  `4`  to quit the menu.

# `search_book_id.py`

## Overview

This script provides a function to search for a book by its ID in a MySQL database. It connects to the database, prompts the user for a book ID, and retrieves and displays the book details if the ID exists.

## Dependencies

-   `mysql.connector`
-   `database.connect`

## Function

### `search_book_id()`

This function connects to the database, prompts the user for a book ID, and retrieves the book details if the ID exists.

#### Steps:

1.  **Print Header:**  Prints a header indicating the start of the book search.
    
2.  **Database Connection:**
    
    -   Connects to the database using  `connect_db()`.
    -   Initializes a cursor for executing SQL queries.
3.  **User Input:**
    
    -   Prompts the user to enter the ID of the book they are looking for.
    -   Strips any leading/trailing whitespace and converts the input to an integer.
4.  **Query Execution:**
    
    -   Executes a query to retrieve all book IDs from the  `books`  table.
    -   Iterates through the result set to check if the entered book ID exists.
5.  **Book Retrieval:**
    
    -   If the book ID exists, executes a query to retrieve all details of the book with the specified ID.
    -   Prints the book details.
    -   Prompts the user to press 'enter' to go back.
6.  **Error Handling:**
    
    -   Catches and prints any  `mysql.connector.Error`  that occurs during the execution.
7.  **Cleanup:**
    
    -   Closes the cursor and the database connection if they are open.

#### Example Usage:

search_book_id()

## Error Handling

-   The function handles  `mysql.connector.Error`  exceptions and prints an error message if an exception occurs.

## Notes

-   The function currently prints the book details directly. It includes a comment suggesting to change the status and author ID to display the author's name instead of the ID.
-   If the entered book ID does not exist, the function prompts the user to press 'enter' to go back to the menu.

# `search_book_title.py`

This module provides functionality to search for a book by its title in a MySQL database.

## Functions

### `search_book_title()`

Prompts the user to enter the title of a book and searches for it in the database. If the book is found, it displays the book's details. If the book is not found, it informs the user and returns to the menu.

#### Usage

search_book_title()

#### Details

1.  **Imports:**
    
    -   `connect_db`  from  `database.connect`: Function to establish a connection to the database.
    -   `Error`  from  `mysql.connector`: Exception class for handling MySQL errors.
2.  **Function Steps:**
    
    -   Prints a header for the books section.
    -   Tries to establish a connection to the database using  `connect_db()`.
    -   Prompts the user to enter the title of the book they are looking for.
    -   Executes a query to fetch all book titles from the  `books`  table.
    -   Iterates through the fetched book titles:
        -   If a match is found, executes a query to fetch all details of the book with the matching title and prints the details.
        -   If no match is found, informs the user that the title doesn't exist.
    -   Handles any MySQL errors that occur during the process.
    -   Ensures that the database connection is closed properly in the  `finally`  block.

#### Example

# Example usage

search_book_title()

When the function is called, it will prompt the user to enter a book title, search for it in the database, and display the book's details if found. If the book is not found, it will inform the user and return to the menu.

# `search_book_author.py`

This script allows users to search for books by author name from a database. It connects to a MySQL database, retrieves author information based on user input, and displays the books written by the selected author.

## Functions

### `search_book_author()`

This function prompts the user to enter the name of an author, searches for authors matching the input, and displays the books written by the selected author.

#### Steps:

1.  **Print Header:**
    
    -   Prints a header indicating the start of the book search process.
2.  **Database Connection:**
    
    -   Establishes a connection to the database using  `connect_db()`.
3.  **User Input:**
    
    -   Prompts the user to enter the name of the author they are looking for.
    -   Converts the input to title case.
4.  **Query Execution:**
    
    -   Executes a query to search for authors whose names match the input.
    -   Fetches and displays the list of matching authors.
5.  **Author Selection:**
    
    -   Prompts the user to select an author from the list.
    -   Executes a query to fetch books written by the selected author.
    -   Displays the list of books.
6.  **Error Handling:**
    
    -   Catches and prints any errors that occur during the database operations.
7.  **Cleanup:**
    
    -   Closes the database cursor and connection.

#### Example Usage:

search_book_author()

## Dependencies

-   `database.connect.connect_db`: Function to establish a database connection.
-   `mysql.connector.Error`: Exception class for handling MySQL errors.

## Error Handling

-   The function catches and prints any  `mysql.connector.Error`  that occurs during the execution of database operations.

## Notes

-   Ensure that the database connection details are correctly configured in the  `connect_db`  function.
-   The script assumes that the database schema includes  `authors`  and  `books`  tables with appropriate fields.

## Sample Output

Books:

------------

Enter the name of the author of the book you're looking for:

J.K. Rowling

1 J.K. Rowling

select the number of the author

1

Book 1: Harry Potter and the Philosopher's Stone

Book 2: Harry Potter and the Chamber of Secrets

...

# `display_books.py`

## Overview

This script connects to a database, retrieves book information, and displays it in a formatted manner. It handles database connections, executes SQL queries, and processes the results to present a list of books along with their details.

## Dependencies

-   `mysql.connector`: Used for connecting to and interacting with a MySQL database.
-   `database.connect`: A module that provides the  `connect_db`  function to establish a database connection.

## Functions

### `books_display()`

This function connects to the database, retrieves book information, and displays it.

#### Functionality:

1.  Prints a header for the book list.
2.  Establishes a connection to the database using  `connect_db()`.
3.  Executes an SQL query to fetch book details.
4.  Iterates over the fetched results and prints each book's details in a formatted manner.
5.  Waits for user input to return to the previous menu.
6.  Handles any database connection errors.
7.  Ensures the database connection is closed properly.

#### SQL Query:

The SQL query retrieves the following details for each book:

-   `book_id`
-   `book_name`
-   `author_name`
-   `publication_date`
-   `status`

#### Example Output:

Books:

---------

Book ID: 1, Book Name: Example Book, Author: John Doe, Year: 2020, Status: available

...

Press 'enter' to go back.

## Error Handling

-   Catches and prints any  `mysql.connector.Error`  that occurs during the database operations.

## Cleanup

-   Ensures that the database connection and cursor are closed properly in the  `finally`  block.

## Usage

To use this script, simply call the  `books_display()`  function. Ensure that the database connection details are correctly configured in the  `connect_db`  function within the  `database.connect`  module.

# `menu.py`  Documentation

## Overview

`menu.py`  is a script that provides a command-line interface (CLI) for user operations. It allows users to add new users, display all users, or quit the application.

## Functions

### `user_operations_menu()`

This function displays a menu to the user and performs actions based on the user's input. It runs in an infinite loop until the user chooses to quit.

#### Menu Options

1.  **Add a new user**: Calls the  `new_user()`  function to add a new user.
2.  **Display all users**: Calls the  `display_users()`  function to display all users.
3.  **Quit**: Exits the menu and terminates the loop.

#### Implementation Details

-   The screen is cleared using  `os.system("cls")`  before displaying the menu and after each operation.
-   User input is taken using the  `input()`  function.
-   Based on the user's input, the corresponding function is called or an error message is displayed for invalid input.

## Imports

-   `os`: Used to clear the screen.
-   `new_user`  from  `app.user_operations.add_new_user`: Function to add a new user.
-   `display_users`  from  `app.user_operations.display_all_users`: Function to display all users.

## Example Usage

To use the  `user_operations_menu`, simply call the function:

user_operations_menu()

This will start the CLI and allow the user to interact with the menu options.

# `add_new_user.py`

This script is responsible for adding a new user to the database. It connects to the database, prompts the user for input, and inserts the new user's name into the  `users`  table.

## Functions

### `new_user()`

This function handles the process of adding a new user to the database.

#### Steps:

1.  **Connect to the Database**:
    
    -   Establishes a connection to the database using the  `connect_db()`  function from the  `database.connect`  module.
    -   Creates a cursor object for executing SQL queries.
2.  **User Input**:
    
    -   Prompts the user to enter the first and last name of the new user.
    -   Formats the input to title case and strips any leading or trailing whitespace.
3.  **Insert User into Database**:
    
    -   Constructs an SQL  `INSERT`  query to add the new user's name to the  `users`  table.
    -   Executes the query with the provided user name.
    -   Commits the transaction to save the changes in the database.
4.  **Confirmation Message**:
    
    -   Displays a confirmation message to the user with a hardcoded customer ID (`user_id = 1`).
    -   Increments the  `user_id`  by 1 (though this incremented value is not used).
5.  **Error Handling**:
    
    -   Catches any  `mysql.connector.Error`  exceptions and prints an error message.
6.  **Cleanup**:
    
    -   Ensures that the cursor and database connection are closed properly in the  `finally`  block.

#### Example Usage:

new_user()

## Dependencies

-   `database.connect.connect_db`: Function to establish a database connection.
-   `mysql.connector.Error`: Exception class for handling MySQL errors.

# `display_all_users.py`

## Overview

This script connects to a MySQL database and displays all users from the  `users`  table. It handles database connection, query execution, and error handling.

## Functions

### `display_users()`

This function connects to the database, retrieves all users, and prints them to the console.

#### Usage

display_users()

#### Description

1.  Prints a header for the users list.
2.  Tries to:
    -   Establish a connection to the database using  `connect_db()`.
    -   Create a cursor object.
    -   Execute a SQL query to select all users from the  `users`  table.
    -   Fetch and print each row of the result.
    -   Wait for user input to go back.
3.  Catches and prints any  `mysql.connector.Error`  that occurs during the process.
4.  Ensures that the database connection and cursor are properly closed in the  `finally`  block.

#### Example

display_users()

## Dependencies

-   `mysql.connector`: Used for connecting to and interacting with the MySQL database.
-   `connect_db`  from  `database.connect`: A function that establishes and returns a database connection.

## Error Handling

-   Catches  `mysql.connector.Error`  and prints the error message.

## Notes

-   Ensure that the  `connect_db`  function is correctly implemented and available in the  `database.connect`  module.
-   The script assumes that the  `users`  table exists in the connected database.

# `menu.py`  Documentation

## Overview

The  `menu.py`  script provides a command-line interface for author operations. It allows users to add new authors, display all authors, or quit the application.

## Functions

### `author_operations_menu()`

This function displays a menu to the user and performs actions based on the user's input. It runs in an infinite loop until the user chooses to quit.

#### Menu Options:

1.  **Add a new author**: Clears the screen and calls the  `new_author`  function.
2.  **Display all authors**: Clears the screen and calls the  `display_authors`  function.
3.  **Quit**: Exits the menu loop.

#### Invalid Input:

If the user enters an invalid option, a message is displayed, and the user is prompted to try again.

## Dependencies

-   **os**: Used to clear the screen with  `os.system("cls")`.
-   **new_author**: Imported from  `app.author_operations.add_new_author`.
-   **display_authors**: Imported from  `app.author_operations.display_all_authors`.

## Example Usage

To use the  `author_operations_menu`  function, simply call it in your main script:

if  __name__  ==  "__main__":

author_operations_menu()
# `add_new_author.py`  Documentation

## Overview

The  `add_new_author.py`  script provides functionality to add a new author to the library database. It connects to the database, takes user input for the author's name and nationality, and inserts this information into the  `authors`  table.

## Functions

### `new_author()`

This function handles the process of adding a new author to the database. It prompts the user for the author's name and nationality, then inserts this data into the  `authors`  table.

#### Steps:

1.  **Connect to Database**: Establishes a connection to the database using the  `connect_db`  function.
2.  **Create Cursor**: Creates a cursor object to execute SQL queries.
3.  **User Input**: Prompts the user to enter the author's name and nationality.
4.  **Insert Query**: Constructs and executes an SQL  `INSERT`  query to add the new author to the  `authors`  table.
5.  **Commit Transaction**: Commits the transaction to save the changes in the database.
6.  **Success Message**: Displays a success message to the user.
7.  **Error Handling**: Catches and prints any database errors that occur during the process.
8.  **Close Connection**: Ensures the database connection is closed properly.

#### Example Usage

To use the  `new_author`  function, simply call it in your main script:

if  __name__  ==  "__main__":

new_author()

## Dependencies

-   **mysql.connector.Error**: Used for handling database errors.
-   **connect_db**: Imported from  `database.connect`, used to establish a connection to the database.

# `display_all_authors.py`

## Overview

This script connects to a MySQL database and retrieves all records from the  `authors`  table. The results are printed to the console.

## Dependencies

-   `mysql.connector`
-   `database.connect`  (custom module for database connection)

## Functions

### `display_authors()`

This function connects to the database, executes a query to fetch all authors, and prints the results.

#### Usage

display_authors()

#### Details

-   **Prints**:
    -   A header "Authors:" followed by a separator line.
    -   Each row from the  `authors`  table.
    -   A prompt for the user to press 'enter' to go back.
-   **Handles**:
    -   Database connection errors.
-   **Ensures**:
    -   The database connection is closed properly in the  `finally`  block.

#### Example

display_authors()

## Error Handling

-   Catches and prints any  `mysql.connector.Error`  exceptions that occur during the database operations.

## Database Connection

-   Uses a custom  `connect_db`  function from the  `database.connect`  module to establish a connection to the database.



