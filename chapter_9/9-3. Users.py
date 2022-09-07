class Users:
    def __init__(self, first_name, last_name, age, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

    def describe_user(self):
        print(f"\nUsers full name is {self.first_name.title()} {self.last_name.title()}.")
        print(f"Users age is {self.age}.")
        print(f"Users nationality is {self.nationality}.\n")

    def greeting_user(self):
        print(f"Hello,welcome back {self.first_name.title()} {self.last_name.title()}.")


user1 = Users(first_name="muhammad", last_name="ali", age=20, nationality="US")
user1.describe_user()
user1.greeting_user()

user2 = Users(first_name="mike", last_name="tyson", age=18, nationality="US")
user2.describe_user()
user2.greeting_user()
