class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"the name of this restaurant is {self.restaurant_name}.")
        print(f"the cuisine type of this restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant is open.")


restaurant1 = Restaurant(restaurant_name="xxxxx", cuisine_type="LA")
restaurant2 = Restaurant(restaurant_name="yyyyy", cuisine_type="CA")
restaurant3 = Restaurant(restaurant_name="zzzzz", cuisine_type="NYC")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()



