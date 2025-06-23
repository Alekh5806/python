# Function with a default country
def describe_city(city, country='India'):
    print(f"{city.title()} is in {country.title()}.")

# Calls
describe_city('ahmedabad')         # Uses default country
describe_city('tokyo', 'japan')    # Overrides default
describe_city('paris', 'france')   # Another custom one