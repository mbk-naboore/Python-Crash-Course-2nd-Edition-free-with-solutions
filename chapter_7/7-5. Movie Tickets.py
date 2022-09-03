while True:
    age = str(input("\nHow old are you [type 'quit' to exit]?\n>>> "))
    if age.strip() == 'quit':
        break

    age = int(age)

    if age < 3:
        print("You get in free!")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
print("thank you for you help have fun.....")
