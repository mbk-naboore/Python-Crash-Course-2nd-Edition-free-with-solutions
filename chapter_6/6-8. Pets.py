pet_1 = {
    'kind of animal': "dog",
    'owner name': "david",
    "age": "5 years"
}
pet_2 = {
    'kind of animal': "cat",
    'owner name': "mike",
    "age": "2 years"
}
pet_3 = {
    'kind of animal': "monkey",
    'owner name': "jack",
    "age": "6 years"
}

pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print(f"\nHere's what I know about {pet['kind of animal'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

