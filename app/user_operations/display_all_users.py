from app.classes.user import users
def display_users():
    print("""
Users:
--------------------
""")
    for user in users:
        user.show_user()
    input("When you're done checking the list of users press 'enter'.\n ")
    return
