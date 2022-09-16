class Employee:

    def __init__(self, first_name, last_name, salary):
        """first name, last name, and salary of the employee"""
        self.first = first_name.title()
        self.last = last_name.title()
        self.salary = salary
        pass

    def give_raise(self, increase=5000):
        """Increase salary by 5000 as a default value."""
        self.salary += increase
        pass

    pass

