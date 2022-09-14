import json

file_name = "username.json"


def get_new_username():
    username = input("What is your name: ")
    with open(file_name, 'w') as f:
        json.dump(username, f)
    return username


def get_stored_username():
    try:
        with open(file_name) as f:
            username = json.load(f)
            return username
    except FileNotFoundError:
        return False


def check_username(username):
    if username:
        flag = input(f"Is [{username}] your username [y/n]? ").lower().strip()
        if flag == 'y':
            print(f"Welcome back, {username}!")
            return True


def greet_user_check_first():
    username = get_stored_username()
    if check_username(username):
        return True
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user_check_first()

