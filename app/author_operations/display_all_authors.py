from app.classes.author import authors
def display_authors():
    print("""
Authors:
------------
""")
    for  author in authors:
        author.show_author()
    input("When you're done checking the list of users press 'enter'.\n ")
    return
