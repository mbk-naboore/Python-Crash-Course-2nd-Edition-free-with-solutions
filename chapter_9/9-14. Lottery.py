import random

possibilities = ["a", "b", "r", "o", "m", 0, 2, 3, 4, 5, 6, 7, 8, 9]
winning = []
while len(winning) < 4:
    winning.append(str(random.choice(possibilities)))
print(f"\nthe winning Lottery card is:  \n\t\t{''.join(winning)}")
