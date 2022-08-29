# Define The list
icecreams_flav = ['chocolate', 'vanilla', 'mango', 'cotton candy']
print("The original list:")
print(icecreams_flav)

# Add some more elements
print("\nUse insertion:")
icecreams_flav[0] = 'strawberry'
print(icecreams_flav)

print("Use append() method:")
icecreams_flav.append('raspberry')
print(icecreams_flav)

print("Use insert() method:")
icecreams_flav.insert(0, 'lemon')
print(icecreams_flav)

# Remove elements
print("\nUse del function (by index):")
del(icecreams_flav[5])
print(icecreams_flav)

print("Use pop() method (by index):")
popped_icecream = icecreams_flav.pop(0)
print(icecreams_flav)
print(popped_icecream)

print("Use remove() method (by value):")
to_remove = 'vanilla'
icecreams_flav.remove(to_remove)
print(icecreams_flav)


# Organise
print("\nUse sorted() function:")
print(sorted(icecreams_flav))
print(sorted(icecreams_flav, reverse=True))


print("Use reverse() method twice:")
icecreams_flav.reverse()
print(icecreams_flav)
icecreams_flav.reverse()
print(icecreams_flav)


print("Use sort() method twice:")
icecreams_flav.sort()
print(icecreams_flav)
icecreams_flav.sort(reverse=True)
print(icecreams_flav)

# Find length
print(f"We ended up with {len(icecreams_flav)} ice creams!")
