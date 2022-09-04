sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

# as long as there (sandwich_orders) list is not empty the loop will work...
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I have made the {sandwich}")
    finished_sandwiches.append(sandwich)
for sandwiches in finished_sandwiches:
    print(f"the finished sandwiches are ::{sandwiches}")

