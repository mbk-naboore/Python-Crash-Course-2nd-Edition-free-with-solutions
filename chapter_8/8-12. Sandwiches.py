def sandwiches_making(*toppings):##Arbitrary parameter
    print("Your sandwich will be ready soon..")
    for topping in toppings:
        print("Adding..", topping)
    print("Your sandwich is ready!")
    print("-"*50)


sandwiches_making("chess", "mushroom", "meat", 'chicken', "BBC sauce")
sandwiches_making("chess", "meat",)
sandwiches_making("mushroom", 'chicken', "BBC sauce")
