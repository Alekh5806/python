# Function to build a car dictionary
def make_car(manufacturer, model, **options):
    car = {
        'manufacturer': manufacturer.title(),
        'model': model.title()
    }
    for key, value in options.items():
        car[key] = value
    return car

# Example call with additional info
car_profile = make_car('tesla', 'model s', color='red', autopilot=True, year=2024)

# Print result
print(car_profile)