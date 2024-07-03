library = []

class Book:
    def __init__(self, title, author, publication_date, status):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.__status = status

    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        self.__status = new_status

    def add_book_to_library(self):
        library.append(self)

    def show_book(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPublication Date: {self.publication_date}\nStatus: {self.get_status()}\n---------")
    

    def borrow_book(self):
        if self.get_status() != "Borrowed":
            self.set_status("Borrowed")
            return {"Message": "The book was succesfuly borrowed. Press 'enter' to return to the menu\n ", "Successful" : True}
        else:
            return {"Message": "The book is not available to borrow. Press 'enter' to return to the menu\n ", "Successful" : False}


    def return_book(self):
        if self.get_status != "Available":
            self.set_status("Available")
            return {"Message": "The book was succesfuly returned. Press 'enter' to return to the menu\n ", "Successful" : True}
        else:
            return {"Message": "The book is not available to borrow. Press 'enter' to return to the menu\n ", "Successful" : False}