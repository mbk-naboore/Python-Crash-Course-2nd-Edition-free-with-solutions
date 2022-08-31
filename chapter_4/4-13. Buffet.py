available_food_only = ("Pizza", "Chicken Nuggets", "Burger", "falafel", "Steak")

print("The restaurant offers the following dishes:")
for food in available_food_only:
    print(food.title())

# Try to modify the first item:
# available_food_only[0] = "Cake"
# (TypeError) is raised

available_food_only = ("pancakes", "Chicken Nuggets", "Burger", "brownie with ice cream", "Steak")
print("\nThe restaurant new menus offers the following dishes:")
for food in available_food_only:
    print(food.title())

