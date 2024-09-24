import subprocess
import os

def add_user_to_group():
    username = input("Enter the name of the user that you want to add to a group: ")

    # Get list of all groups
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
    print("Enter a list of groups to add the user to")
    print("The list should be separated by spaces, for example:\r\ngroup1 group2 group3")
    print("The available groups are:\r\n" + output)

    chosenGroups = input("Groups: ").split(" ")
    availableGroups = output.split(" ")
    
    print("Add To:")
    groupString = ""
    
    for grp in chosenGroups:
        if grp in availableGroups:
            print("- Existing Group: " + grp)
            groupString += grp + ","
        else:
            print("- New Group: " + grp)
            groupString += grp + ","

    groupString = groupString[:-1]  # Remove the last comma

    confirm = ""
    while confirm not in ["Y", "N"]:
        confirm = input(f"Add user '{username}' to these groups? (Y/N): ").upper()

    if confirm == "N":
        print(f"User '{username}' not added.")
    elif confirm == "Y":
        os.system(f"sudo usermod -aG {groupString} {username}")
        print(f"User '{username}' added to groups: {groupString}")

add_user_to_group()
