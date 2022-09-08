class Restaurant:
    """A class to describe a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise some attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"the name of this restaurant is {self.restaurant_name}.")
        print(f"the cuisine type of this restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant is open.")

    def set_number_served(self, customers):
        """Set the number of customers served"""
        self.number_served = customers

    def increment_number_served(self, increment_customers):
        """Increment the number of customers served"""
        self.number_served += increment_customers


restaurant1 = Restaurant('don giovanni', 'italian')

# printing the number of served customers , chaining that value and reprinting it...
print(restaurant1.number_served)
restaurant1.number_served = 5
print(restaurant1.number_served)


# Set number of customers served using the set_number_served() method...
restaurant1.set_number_served(14)
print(restaurant1.number_served)


# Increment number of customers served using the increment_number_served() method...
restaurant1.increment_number_served(21)
print(restaurant1.number_served)
