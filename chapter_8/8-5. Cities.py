def describe_city(name_city, country="UK"):
    print(f"{name_city.title().strip()} is in {country}")
    pass


describe_city(name_city="Nottingham")
describe_city("London")
describe_city("LA", "USA")
