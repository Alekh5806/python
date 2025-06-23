import json

filename = 'favorite_number.json'

# Store the number
number = input("What is your favorite number? ")
with open(filename, 'w') as f:
    json.dump(number, f)

# Read the number
with open(filename) as f:
    fav_number = json.load(f)
    print(f"I know your favorite number! It’s {fav_number}.")