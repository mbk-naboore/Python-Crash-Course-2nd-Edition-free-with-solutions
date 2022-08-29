locations = ['Paris', 'NYC', 'guam', 'pyramids', 'monaco']

print("The Original order is:", locations)

print("\nThe Alphabetical order:", sorted(locations))


print("\nThe Original order is still:")
print(locations)

print("\nNow The Reverse alphabetical order is:")
print(sorted(locations, reverse=True))

print("\nOriginal order is still:")
print(locations)

print("\nThe Reversed List:")
locations.reverse()
print(locations)

print("\nReturn to the Original order:")
locations.reverse()
print(locations)

print("\nAlphabetical Order of the elements:")
locations.sort()
print(locations)

print("\nReverse alphabetical order :")
locations.sort(reverse=True)
print(locations)
