from app.classes.user import User
def import_users():
    with open("users.txt", "r") as file:
        for line in file:
            name, user_id = line.split(';')
            new_user = User(name, user_id.strip())
            new_user.new_user()