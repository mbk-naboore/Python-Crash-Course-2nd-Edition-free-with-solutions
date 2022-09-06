def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_info_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }

    for key, value in options.items():
        car_info_dict[key] = value

    return car_info_dict


car1 = make_car('subaru', 'Toyota', color='SkyBlue', tow_package=True)
print(car1)


