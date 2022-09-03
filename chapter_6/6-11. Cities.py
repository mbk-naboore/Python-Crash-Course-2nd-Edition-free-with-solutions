city1 = {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
        }
city2 = {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
        }
city3 = {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
        }
cities = {
    'santiago': city1,
    'talkeetna': city2,
    'kathmandu': city3
    }


for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {mountains} mountains are nearby.")

