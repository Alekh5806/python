# Create dictionaries for pets
pet1 = {
    'animal_type': 'dog',
    'name': 'Bruno',
    'owner': 'Alekh'
}

pet2 = {
    'animal_type': 'cat',
    'name': 'Milo',
    'owner': 'Krunal'
}

pet3 = {
    'animal_type': 'rabbit',
    'name': 'Snowy',
    'owner': 'Devansh'
}

# Store all pets in a list
pets = [pet1, pet2, pet3]

# Loop through the list and print pet details
for pet in pets:
    print(f"\n{pet['name'].title()} is a {pet['animal_type']} owned by {pet['owner']}.")