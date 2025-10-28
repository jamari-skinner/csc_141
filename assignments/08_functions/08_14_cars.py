# 8-14 Cars

def make_car(manufacturer, model, **options):
    """Build a dictionary containing everything we know about a car."""
    car_dict = {
        'manufacturer': manufacturer,
        'model': model,
    }
    for key, value in options.items():
        car_dict[key] = value
    return car_dict

car_1 = make_car('nissan', 's15.......', color='blue', tow_package=True)
car_2 = make_car('tesla', 'model s', color='red', autopilot=True)

print(car_1)
print(car_2)
