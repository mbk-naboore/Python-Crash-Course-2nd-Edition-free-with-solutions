file_list_names = ['The_Life_and_Love_of_the_Insect_10_10.txt', "The_Snake's_Pass_10_10.txt", "Alice's_Adventures_in_Wonderland_10_10.txt"]

for file in file_list_names:
    try:
        with open(file, 'r', encoding="UTF-8") as f:
            contents = f.read().strip()
    except FileNotFoundError:
        print(f"\nThe file ({file}) is not available.")
    except UnicodeDecodeError:
        print(f"\nThe file ({file}) cannot be read because of some encoding mismatch problem.")
    else:
        print(f"\nAnalysing the content of ({file}):")
        print(f"The number of occurrences of ('the') is: {contents.lower().count('the')}.")
        print(f"The number occurrences of ('the ') is: {contents.lower().count('the ')}.")
