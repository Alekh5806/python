# Function that returns city and country in formatted string
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

# Calls and printing results
print(city_country('tokyo', 'japan'))
print(city_country('paris', 'france'))
print(city_country('mehsana', 'india'))