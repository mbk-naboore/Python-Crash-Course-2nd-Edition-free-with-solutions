import json


def user_fav_number():
    file_name = "fav_number.json"
    try:
        with open(file_name, "r") as f:
            number = json.load(f)
            pass
        print(f"\nI know what is your favorite number! It is ( {number} ).")

    except FileNotFoundError:
        number = int(input("\nPlease tell us your favorite number:\t"))
        with open(file_name, "w") as f:
            json.dump(number, f)
            pass
        print("\nI will remember that number for the next time...")


user_fav_number()

