rivers_dictionary = {
    'nile': 'egypt',
    "amazon": "barazil"
}
for rivers, country in rivers_dictionary.items():
    print(f"the {rivers.title()} runs through{country.title()}")
print("-----------------------------------------------------------------")
for river in rivers_dictionary.keys():
    print(river.title())
print("-----------------------------------------------------------------")
for value in rivers_dictionary.values():
    print(value.title())
