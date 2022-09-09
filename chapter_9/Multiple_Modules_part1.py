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
