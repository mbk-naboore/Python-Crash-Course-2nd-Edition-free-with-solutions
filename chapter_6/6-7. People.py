friend_1 = {
    "first_name": "Muhammad Ali",
    "last_name": "clay",
    "age": 30,
    "city": "NYC"
}
friend_2 = {"first_name": "james",
            "last_name": "bond",
            "age": 32,
            "city": "LA"
            }
friend_3 = {"first_name": "mike",
            "last_name": "tyson",
            "age": 25,
            "city": "CA"
            }
friends = [friend_1, friend_2, friend_3]
for friend in friends:
    name = (f"{friend['first_name'].title()} {friend['last_name'].title()}")
    age = friend['age']
    city = friend['city'].title()
    print(f"{name},from {city}, is {age} years old.")

