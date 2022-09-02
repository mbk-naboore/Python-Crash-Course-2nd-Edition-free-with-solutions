glossary = {
    'dictionary': 'is a collection of key-value pairs.',
    'list': 'is a collection of items ,accessed using the index of the item.',
    'tuple': 'An Immutable list.',
    'conditional test': 'Code that produces True or False answer.',
    'for loop': 'a block of code that will be repeated (n) number of times.'
    }

print()
for key, value in glossary.items():
    print(f"{key.title()} --> {value.title()}")
