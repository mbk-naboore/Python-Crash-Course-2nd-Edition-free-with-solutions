favorite_lanuages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'pyhton'
}

pool_list = ['mario', 'phil', 'kevin', 'jen']
for names in favorite_lanuages.keys():
    if names in pool_list:
        print(f"thank you {names.title()} for the respond.")
    else:
        print(f"please {names.title()} can you take the pool.")
