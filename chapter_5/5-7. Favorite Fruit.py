# rather than writing hundreds of if and elif statements you can just change
# the value of variable (fruit = "any_fruit") and you will see the results...

favorite_fruits = ['apple', 'banana', 'pear', 'grape', 'pineapple']
fruit = "pineapple"
if fruit in favorite_fruits:
    print(f"you really like {fruit}.")
