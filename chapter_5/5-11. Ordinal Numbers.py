
# Create the list
numbers = list(range(1, 10))


# Loops for ordinal endings
for i in numbers:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")
