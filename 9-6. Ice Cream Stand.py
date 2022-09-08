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


class IceCreamStand(Restaurant):
    """a modified restaurant type from the main superclass (Restaurant) """
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [*flavors]

    def display_flavors_list(self):
        print("All the flavors we have are ::\t")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


Ice_cream1 = IceCreamStand("TheIceCreamRestaurant", "IceCream", "vanilla", "Chocolate", "milk", "cotton-candy", "caramel")

Ice_cream1.describe_restaurant()
Ice_cream1.display_flavors_list()

# this will display the list(attribute) flavors this obj has
print(Ice_cream1.flavors)

