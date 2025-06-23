
person1 = {
    'first_name': 'Alekh',
    'last_name': 'Patel',
    'age': 20,
    'city': 'Mehsana'
}

person2 = {
    'first_name': 'Krunal',
    'last_name': 'Goswami',
    'age': 21,
    'city': 'Ahmedabad'
}

person3 = {
    'first_name': 'Devansh',
    'last_name': 'Shah',
    'age': 22,
    'city': 'Rajkot'
}


people = [person1, person2, person3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    
    print(f"\nName: {full_name}")
    print(f"Age: {age}")
    print(f"City: {city}")