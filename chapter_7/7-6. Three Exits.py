counter = 1
while counter <= 5:
    age = str(input("How old are you?[Enter 'quit' when you are finished]\n>>> "))
    if age.strip() == 'quit':
        break
    
    age = int(age)

    # counter = counter+1
    counter += 1
    # this is another way of adding to the variable(updating it's value)...

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
print("thank you for you help have fun.....")
