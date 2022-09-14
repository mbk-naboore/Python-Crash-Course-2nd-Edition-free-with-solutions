import json


def fav_number_input():
    number = int(input("Please tell us your favorite number:\t"))
    with open("fav_number.json", "w") as f:
        json.dump(number, f)
        pass


def fav_number_is():
    try:
        with open("fav_number.json", "r") as f:
            number = json.load(f)
            print(f"I know what is your favorite number! It is ( {number} ).")
    except FileNotFoundError:
        pass


fav_number_input()

fav_number_is()

