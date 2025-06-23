# Dictionary of cities with details
cities = {
    'mehsana': {
        'country': 'india',
        'population': '185,000',
        'fact': 'Known for Modhera Sun Temple nearby.'
    },
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'Home to the Eiffel Tower.'
    },
    'tokyo': {
        'country': 'japan',
        'population': '13.9 million',
        'fact': 'World’s most populous city.'
    }
}

# Print city information
for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")