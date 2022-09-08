class Users:
    def __init__(self, first_name, last_name, age, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nUsers full name is {self.first_name.title()} {self.last_name.title()}.")
        print(f"Users age is {self.age}.")
        print(f"Users nationality is {self.nationality}.\n")

    def greeting_user(self):
        print(f"Hello,welcome back {self.first_name.title()} {self.last_name.title()}.")

    def increment_login_attempts(self):
        self.login_attempts += self.login_attempts
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


user1 = Users(first_name="mbk", last_name="naboore", age=18, nationality="US")
user1.describe_user()
user1.greeting_user()

print("\nwe are going to make 3 login attempts...")
print("1st login attempt:\n\t\t", user1.increment_login_attempts())
print("2nd login attempt:\n\t\t", user1.increment_login_attempts())
print("3rd login attempt:\n\t\t", user1.increment_login_attempts())

print("---------------------------------------------------------------")

print("\nI am going to reset the login attempts number:")
print("the login attempts are now:\n\t\t", user1.reset_login_attempts())
