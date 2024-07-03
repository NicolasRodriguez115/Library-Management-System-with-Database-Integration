from app.classes.author import Author
def import_authors():
    with open("authors.txt", "r") as file:
        for line in file:
            name, nationality = line.split(';')
            new_author = Author(name, nationality)
            new_author.new_author()