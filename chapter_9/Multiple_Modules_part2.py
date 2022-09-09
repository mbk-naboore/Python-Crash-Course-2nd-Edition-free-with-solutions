from Multiple_Modules_part1 import Users


class Admin(Users):
    """the privileges of the admin user"""
    def __init__(self, first_name, last_name, age, nationality):
        super().__init__(first_name, last_name, age, nationality)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ["admin can add post", "admin can delete post", "admin can ban user"]

    def show_privileges(self):
        print(f"The privileges for this User are:")
        for privilege in self.privileges:
            print(f"-{privilege}")
