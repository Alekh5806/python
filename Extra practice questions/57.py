# Extended version of the 'cities' dictionary
cities = {
    'mehsana': {
        'country': 'india',
        'population': '185,000',
        'language': 'Gujarati',
        'famous_food': 'Bhaji Pav',
        'fact': 'Known for Modhera Sun Temple nearby.'
    },
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'language': 'French',
        'famous_food': 'Croissant',
        'fact': 'Home to the Eiffel Tower.'
    },
    'tokyo': {
        'country': 'japan',
        'population': '13.9 million',
        'language': 'Japanese',
        'famous_food': 'Sushi',
        'fact': 'World’s most populous city.'
    },
    'new york': {
        'country': 'usa',
        'population': '8.5 million',
        'language': 'English',
        'famous_food': 'Pizza',
        'fact': 'Famous for Times Square and Wall Street.'
    }
}

# Display detailed info for each city
for city, details in cities.items():
    print(f"\n📍 {city.title()} — {details['country'].title()}")
    print(f"  Population  : {details['population']}")
    print(f"  Language    : {details['language']}")
    print(f"  Famous Food : {details['famous_food']}")
    print(f"  Fact        : {details['fact']}")