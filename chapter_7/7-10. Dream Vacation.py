name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "
users_info = {}
while True:
    name = input(name_prompt)
    place = input(place_prompt)
    users_info[name] = place
    continue_or_not = input(continue_prompt)
    if continue_or_not.strip() == "no":
        break
print("\n-------- Results --------")
for names, places in users_info.items():
    print(f"{names} loves {places}")
