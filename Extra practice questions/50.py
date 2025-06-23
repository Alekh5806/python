# Exercise 6-5: Rivers, where you’ll use a dictionary to store the name of three rivers and the country each river runs through.


# Dictionary of rivers and the countries they flow through
rivers = {
    'nile': 'egypt',
    'ganges': 'india',
    'amazon': 'brazil'
}


for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")


print("\nRivers included in the dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nCountries mentioned in the dictionary:")
for country in rivers.values():
    print(country.title())