# Function to show magicians
def show_magicians(magicians):
    for magician in magicians:
        print(f"{magician.title()}")

# List of magicians
magician_names = ['houdini', 'criss angel', 'dynamo', 'p. c. sorcar']

# Call the function
show_magicians(magician_names)