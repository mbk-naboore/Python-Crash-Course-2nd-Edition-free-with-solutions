while True:
    topping = input("Give us you favorite toppings [type 'quit' to exit]:\n>>> ")
    if topping.strip() == "quit":
        print("\nThank you very much, The pizza will be ready in minutes.\n")
        break
    else:
        print(f"\nAdding {topping}\n")
