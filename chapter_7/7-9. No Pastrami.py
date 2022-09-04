sandwich_orders = ['pastrami', 'veggie', 'grilled cheese', 'pastrami', 'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []
print("the deli has run out of pastrami...sorry for that")
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    sandwich = sandwich_orders.pop(0)
    print(f"I have made the {sandwich}")
    finished_sandwiches.append(sandwich)
for sandwiches in finished_sandwiches:
    print(f"the finished sandwiches are ::{sandwiches}")

