# Exercise 6-6: Polling — this one builds on previous exercises where you used a dictionary to store people’s favorite programming languages. Now you’ll check who has already taken the poll and who hasn’t.


# People who have already taken the poll
favorite_languages = {
    'alekh': 'python',
    'krunal': 'c++',
    'mihir': 'java',
    'devansh': 'javascript'
}

# List of people to check
people_to_poll = ['alekh', 'nina', 'krunal', 'sahil', 'devansh']

# Polling logic
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll.")
    else:
        print(f"{person.title()}, please take our poll about your favorite programming language!")