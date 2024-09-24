import os
def remove_user():
    confirm = "N"
    while confirm != "Y":
          username = input("Enter thename of the user to remove: ")
          print("Use the username '" + username + "'? (Y/N)")
          confirm = input().upper()
    os.system("sudo userdel -r " + username)

remove_user()
