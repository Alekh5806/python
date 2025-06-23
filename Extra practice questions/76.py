# Function to show magicians
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# Function that returns a new list with "The Great"
def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append("The Great " + magician)
    return great_magicians

# Original list
magician_names = ['houdini', 'criss angel', 'dynamo', 'p. c. sorcar']

# Create new list
great_magicians = make_great(magician_names[:])  # Passing a copy

# Show both lists
print("Original Magicians:")
show_magicians(magician_names)

print("\nGreat Magicians:")
show_magicians(great_magicians)