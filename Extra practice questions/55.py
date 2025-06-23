
favorite_numbers = {
    'alekh': [7, 9],
    'krunal': [4, 8, 2],
    'mihir': [1],
    'devansh': [3, 5],
    'sahil': [6, 12]
}


for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")