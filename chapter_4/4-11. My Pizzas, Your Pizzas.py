pizzas = ['Neapolitan Pizza', 'Chicago Pizza', 'New York-Style Pizza']

# making a copy of the list
friend_pizzas = pizzas[:]

# adding to the original list
pizzas.append("Chicken BBQ Pizza")

# adding to the copy list
friend_pizzas.append("All Meat Lover Pizza")


print("My favorite pizzas are:")
for my_pizza in pizzas:
    print(my_pizza)


print("\nMy friend’s favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
