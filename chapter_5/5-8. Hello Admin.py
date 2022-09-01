username_list = ["mike", "john", "admin", "david", "dobrik"]

for users in username_list:
    if users == "admin":
        print("Hello ADMIN,would you like to see a status report?")
    else:
        print(f"Hello {users.title()}, thank you for logging in again.")
