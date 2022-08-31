my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for the_my_foods in my_foods:
    print(the_my_foods)

print("\nMy friend's favorite foods are:")
for the_friends_food in friend_foods:
    print(the_friends_food)
    