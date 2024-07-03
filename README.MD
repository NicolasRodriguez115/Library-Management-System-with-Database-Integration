# Library Management System: Main Menu

The main menu of the Library Management System provides users with options to perform various operations related to books, users, authors, and library management. Users can choose from the following menu items:

1.  **Book Operations**
    
    -   Access book-related functionalities, such as adding, searching, borrowing, and returning books.
    -   Invokes the  `book_operations_menu()`  function.
2.  **User Operations**
    
    -   Perform user-related tasks, including user registration, login, and profile management.
    -   Invokes the  `user_operations_menu()`  function.
3.  **Author Operations**
    
    -   Manage author information, add new authors, and view author details.
    -   Invokes the  `author_operations_menu()`  function.
4.  **Import Existing Library**
    
    -   Import an existing library from an external source (e.g., a text file).
    -   Invokes the  `import_library()`  function.
5.  **Quit**
    
    -   Exit the application and return to the system.

# Library Management System: Book Operations Menu

The book operations menu allows users to perform actions related to managing books within the library. Users can choose from the following options:

1.  **Add a New Book**
    
    -   Allows users to add a new book to the library.
    -   Invokes the  `add_new_book()`  function.
2.  **Borrow a Book**
    
    -   Enables users to borrow a book from the library.
    -   Invokes the  `borrow_book()`  function.
3.  **Return a Book**
    
    -   Allows users to return a borrowed book to the library.
    -   Invokes the  `return_book()`  function.
4.  **Search for a Book**
    
    -   Provides a search functionality to find specific books.
    -   Invokes the  `search_for_book()`  function.
5.  **Display All Books**
    
    -   Shows a list of all available books in the library.
    -   Invokes the  `display_books()`  function.
6.  **Quit**
    
    -   Exits the book operations menu and returns to the main menu.

# Library Management System: Add a New Book

The  `new_book()`  function enables users to add a new book to the library. Here’s how it works:

1.  **Input Prompt**:
    
    -   The user is prompted to provide the following information about the book:
        -   Title
        -   Author’s name
        -   Publication date
2.  **Book Creation**:
    
    -   A new  `Book`  object is created with the provided details.
    -   The book’s status is set to “Available.”
    -   The book is added to the library using the  `add_book_to_library()`  method.
3.  **Author Handling**:
    
    -   If the author already exists in the system (based on the provided author name), the book is associated with that author.
    -   If the author is not registered, the user is prompted to enter additional information:
        -   Nationality of the author
        -   A new  `Author`  object is created and added to the system.
        -   The book is associated with the newly created author.
4.  **User Interaction**:
    
    -   The user receives appropriate messages indicating the success of adding the book.
    -   Pressing “Enter” allows the user to return to the previous menu.

# Library Management System: Borrow a Book

The  `borrow_book()`  function enables users to borrow a book from the library. Here’s how it works:

1.  **Input Prompt**:
    
    -   The user is prompted to provide the following information about the book:
        -   Title
        -   Author’s name
        -   User ID (if available; otherwise, the user can press ‘enter’)
2.  **Book Verification**:
    
    -   The function checks if the provided book title and author match any book in the library.
    -   If a match is found, the book’s status is updated to “Borrowed.”
    -   The user’s borrowed book list is updated (if a valid user ID is provided).
3.  **Handling Invalid Input**:
    
    -   If the book information doesn’t match any book in the library, the user is given the option to try again or exit.
4.  **User Interaction**:
    
    -   The user receives appropriate messages indicating the success of borrowing the book.
    -   Pressing “Enter” allows the user to return to the previous menu.

The  `return_book()`  function enables users to return a borrowed book to the library. Here’s how it works:

1.  **Input Prompt**:
    
    -   The user is prompted to provide the following information about the book:
        -   Title
        -   Author’s name
        -   User ID (if available; otherwise, the user can press ‘enter’)
2.  **Book Verification**:
    
    -   The function checks if the provided book title and author match any borrowed book in the library.
    -   If a match is found, the book’s status is updated to “Available.”
    -   The user’s borrowed book list is updated (if a valid user ID is provided).
3.  **Handling Invalid Input**:
    
    -   If the book information doesn’t match any borrowed book in the library, the user is given the option to try again or exit.
4.  **User Interaction**:
    
    -   The user receives appropriate messages indicating the success of returning the book.
    -   Pressing “Enter” allows the user to return to the previous menu.

# Library Management System: Return a Book

The  `return_book()`  function enables users to return a borrowed book to the library. Here’s how it works:

1.  **Input Prompt**:
    
    -   The user is prompted to provide the following information about the book:
        -   Title
        -   Author’s name
        -   User ID (if available; otherwise, the user can press ‘enter’)
2.  **Book Verification**:
    
    -   The function checks if the provided book title and author match any borrowed book in the library.
    -   If a match is found, the book’s status is updated to “Available.”
    -   The user’s borrowed book list is updated (if a valid user ID is provided).
3.  **Handling Invalid Input**:
    
    -   If the book information doesn’t match any borrowed book in the library, the user is given the option to try again or exit.
4.  **User Interaction**:
    
    -   The user receives appropriate messages indicating the success of returning the book.
    -   Pressing “Enter” allows the user to return to the previous menu.

# Library Management System: Search for a Book

1.  **Input Prompt**:
    
    -   The user is prompted to enter the title of the book they want to search for.
2.  **Search Process**:
    
    -   The function iterates through the library’s collection of books.
    -   If a book with the specified title is found, its details (title, author, publication date, and status) are displayed.
    -   If no matching book is found, an appropriate message is shown.
3.  **User Interaction**:
    
    -   The user can press “Enter” to return to the previous menu.

# Library Management System: Display Books

The  `books_display()`  function displays information about all books in the library. It iterates through the  `library`  and calls the  `show_book()`  method for each book.

# Library Management System: User Operations Menu

The  `user_operations_menu()`  function provides a menu for user-related operations in the Library Management System. Users can choose from various user-related functionalities. Let’s break down each option:

1.  **Add a New User**
    
    -   Allows users to add a new user to the library system.
    -   Calls the  `new_user()`  function.
    -   Clears the screen after execution.
2.  **View User Details**
    
    -   Displays detailed information about a specific user.
    -   Invokes the  `user_details()`  function.
    -   Clears the screen after execution.
3.  **Display All Users**
    
    -   Lists information about all users in the library.
    -   Calls the  `display_users()`  function.
    -   Clears the screen after execution.
4.  **Quit**
    
    -   Exits the user operations menu and returns to the main menu.

# Library Management System: Add New user

The  `new_user()`  function allows you to create a new user for the library system. It follows these steps:

1.  **Input User Details**
    
    -   Asks the user to enter the first and last name of the user.
    -   Capitalizes the input to ensure consistent formatting.
    -   Generates a random customer ID for the user.
2.  **Create User Object**
    
    -   Creates a new  `User`  object with the provided name and generated customer ID.
    -   Calls the  `new_user()`  method on the user object to add it to the library system.
3.  **Confirmation**
    
    -   Displays a success message with the user’s name and customer ID.
    -   Waits for the user to press ‘enter’ before returning.

# Library Management System: User Details

The  `user_details()`  function allows you to view detailed information about a specific user based on their user ID. Here’s how it works:

1.  **Input User ID**
    
    -   Asks the user to enter the ID of the user they want to look up.
    -   The user should provide a valid user ID associated with an existing user.
2.  **Search for User**
    
    -   Iterates through the list of users.
    -   Compares the provided user ID with the IDs of existing users.
    -   If a match is found, displays detailed information about that user.
    -   If no match is found, informs the user that the provided ID is not associated with any current user.
3.  **Confirmation and Return**
    
    -   After displaying user details (if applicable), waits for the user to press ‘enter’ before returning to the main menu.

# Library Management System: Display All Users

The  `display_users()`  function lists information about all users in the library. It iterates through the  `users`  list and calls the  `show_user()`  method for each user.

# Library Management System: Author Operations

The  `author_operations_menu()`  function provides a menu for author-related operations in the Library Management System. Users can choose from various author-related functionalities. Let’s break down each option:

1.  **Add a New Author**
    
    -   Allows users to add a new author to the library system.
    -   Calls the  `new_author()`  function.
    -   Clears the screen after execution.
2.  **View Author Details**
    
    -   Displays detailed information about a specific author.
    -   Invokes the  `author_details()`  function.
    -   Clears the screen after execution.
3.  **Display All Authors**
    
    -   Lists information about all authors in the library.
    -   Calls the  `display_authors()`  function.
    -   Clears the screen after execution.
4.  **Quit**
    
    -   Exits the author operations menu and returns to the main menu.

# Library Management System: Add New Author

The  `new_author()`  function allows you to add a new author to the library system. Here’s how it works:

1.  **Input Author Details**
    
    -   Asks the user to enter the first and last name of the author.
    -   Capitalizes the input to ensure consistent formatting.
    -   Also asks for the nationality of the author.
2.  **Create Author Object**
    
    -   Creates a new  `Author`  object with the provided name and nationality.
    -   Calls the  `new_author()`  method on the author object to add it to the library system.
3.  **Confirmation**
    
    -   Displays a success message indicating that the author has been added.
    -   Waits for the user to press ‘enter’ before returning to the main menu.

# Library Management System: View Authors Details

The  `author_details()`  function allows you to view detailed information about a specific author based on their first and last name. Here’s how it works:

1.  **Input Author Name**
    
    -   Asks the user to enter the first and last name of the author they want to look up.
    -   Capitalizes the input to ensure consistent formatting.
2.  **Search for Author**
    
    -   Iterates through the list of authors.
    -   Compares the provided author name with the names of existing authors.
    -   If a match is found, displays detailed information about that author.
    -   If no match is found, informs the user that the provided author is not registered in the library yet.
3.  **Confirmation and Return**
    
    -   After displaying author details (if applicable), waits for the user to press ‘enter’ before returning to the main menu.

# Library Management System: Display Authors

The `display_authors()` function lists information about all authors in the library. It iterates through the `authors` list and calls the `show_author()` method for each author.

# Library Management System: Importing

## Introduction
This library management system is designed to handle authors, books, and users. It allows importing data from text files and populating the library with relevant information.

## Code Overview
The provided code snippet consists of three main functions:
1. `import_authors()`: Reads author data from "authors.txt" and creates `Author` objects.
2. `import_books()`: Reads book data from "books.txt" and creates `Book` objects. It also associates books with their respective authors.
3. `import_users()`: Reads user data from "users.txt" and creates `User` objects.

## Usage
1. **Importing Authors:**
   - The `import_authors()` function reads data from "authors.txt" (formatted as "name;nationality") and creates `Author` objects.
   - Each line in the file represents an author, and the data is split using a semicolon (;).
   - The `new_author()` method is called to create a new author instance.

2. **Importing Books:**
   - The `import_books()` function reads data from "books.txt" (formatted as "title;author;publication_date;status") and creates `Book` objects.
   - It also associates each book with its corresponding author.
   - The `add_book_to_library()` method is called to add the book to the library.
   - Note that the `authors` list (imported from the `author` module) is used to find the author associated with each book.

3. **Importing Users:**
   - The `import_users()` function reads data from "users.txt" (formatted as "name;user_id") and creates `User` objects.
   - The `new_user()` method is called to create a new user instance.

4. **Running the Import:**
   - To import the entire library, call the `import_library()` function.
   - After importing, the user will receive a message indicating successful import.

## File Formats
- "authors.txt": Each line contains author data in the format "name;nationality".
- "books.txt": Each line contains book data in the format "title;author;publication_date;status".
- "users.txt": Each line contains user data in the format "name;user_id".

## Notes
- Make sure the file paths ("authors.txt", "books.txt", and "users.txt") are correct and accessible.

