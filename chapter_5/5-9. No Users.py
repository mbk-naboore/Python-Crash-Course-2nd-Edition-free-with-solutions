# username_list = ["mike", "john", "admin", "david", "dobrik"]
username_list = []

# python will give the empty list a False statement..
# hear it means if list is not empty go through that for loop if is empty go to else.
if username_list:
    for users in username_list:
        if users == "admin":
            print("Hello ADMIN,would you like to see a status report?")
        else:
            print(f"Hello {users.title()}, thank you for logging in again.")
else:
    print("We need to find some users...")
