favorite_number = {
    'jen': [7, 5],
    'sarah': [3, 1],
    'edward': [2, 8],
    'phil': [1, 7]
}

for names, numbers in favorite_number.items():
    print(names+":")
    for number in numbers:
        print(">>>", number)
    print()

