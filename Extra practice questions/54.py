
favorite_places = {
    'alekh': ['manali', 'goa', 'ladakh'],
    'krunal': ['dubai', 'maldives'],
    'devansh': ['paris']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")