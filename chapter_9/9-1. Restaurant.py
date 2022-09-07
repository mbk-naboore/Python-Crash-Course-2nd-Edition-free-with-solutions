class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"the name of this restaurant is {self.restaurant_name}.")
        print(f"the cuisine type of this restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant is open.")


restaurant = Restaurant(restaurant_name="xxxxx", cuisine_type="LA")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()



