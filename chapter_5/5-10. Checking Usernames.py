current_users = ["mike", "john", "admin", "david", "dobrik"]
new_users = ["tyson", "jack", "david", "mbk-naboore", "mike"]

for users in new_users:
    if users in current_users:
        print(f"sorry, you need to enter a new username....because {users} is taken already...")
    else:
        print(f"you can use {users} it is available....")
