users = []
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.__user_id = user_id
        self.borrowed_books = []
    
    def get_user_id(self):
        return self.__user_id
    
    def new_user(self):
        users.append(self)

    def show_user(self):
        print(f"Name: {self.name}\nID: {self.get_user_id()}\n--------------")

    def display_borrowed_books(self):
        for book in self.borrowed_books:
            print(book)


    def user_details(self):
        print(f"{self.name}:\n User ID: {self.get_user_id}\n List of books in their possession:")
        self.display_borrowed_books()

    def book_borrowed(self, book):
        self.borrowed_books.append(book)

    def book_returned(self, book):
        self.borrowed_books.remove(book)