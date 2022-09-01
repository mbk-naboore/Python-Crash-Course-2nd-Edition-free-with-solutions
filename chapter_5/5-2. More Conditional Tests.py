# string:
item = "class"
print("Test 1--> Is item == \"class\"? I predict True.")
print(item == "class")
print("Test 2--> Is item != '\"class\"? I predict False.")
print(item != "class")

# strings using the lower() method:
name = 'Muhammad Ali'
print("Test 3--> Is name = 'Muhammad Ali' not using lower()? I predict False.")
print(name == 'Muhammad Ali')
print("Test 4--> Is name = 'Muhammad Ali' using lower()? I predict True.")
print(name.lower() == 'Muhammad Ali')

# Numerical tests
muhammad_ali_height = 180
mike_tyson_height = 170
print("Test 5--> Is Muhammad Ali taller than 175cm? I predict True.")
print(muhammad_ali_height > 175)
print("Test 6--> Is Mike Tyson taller than 175cm? I predict False.")
print(mike_tyson_height > 175)

# Using the operators (and) and (or):
print("Test 7--> Are both Muhammad Ali and Mike Tyson taller than or equal to 170 cm? I "
      "predict True.")
print((muhammad_ali_height >= 170) and (mike_tyson_height >= 170))
print("Test 8--> Are both Muhammad Ali and Mike Tyson taller than or equal to 180 cm? I "
      "predict False.")
print((muhammad_ali_height >= 180) and (mike_tyson_height >= 180))
print("Test 9--> Are Muhammad Ali or Mike Tyson taller than 175 cm? I "
      "predict True.")
print((muhammad_ali_height > 175) or (mike_tyson_height > 175))
print("Test 10--> Are Muhammad Ali or Mike Tyson taller than 180 cm? I "
      "predict False.")
print((muhammad_ali_height > 180) and (mike_tyson_height > 180))


# Item in a list
plants = ['Windows', 'IOS', 'linux']
print("Test 11--> Is Windows in the list? I predict True.")
print('Windows' in plants)
print("Test 12--> Is linux in the list? I predict False.")
print('linux' in plants)


# Item not in a list
print("Test 13--> Is Android not in the list? I predict True.")
print('Android' not in plants)
print("Test 14--> Is IOS not in the list? I predict False.")
print('IOS' not in plants)
