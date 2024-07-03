from app.classes.user import users
def user_details():
    select_user = input("Enter the ID of the user to see their information\n").strip()
    
    for user in users:
        if user.get_user_id().strip() == select_user:
            user.user_details()
            input("Press 'enter' to go back.\n ")
            return
        
    input("That isn't an ID associated to a current user. You'll return to the main menu after pressing 'enter'\n ")
    return