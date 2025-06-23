# Function to show magicians
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# Function to make magicians great
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i]

# Original list
magician_names = ['houdini', 'criss angel', 'dynamo', 'p. c. sorcar']

# Modify list
make_great(magician_names)

# Display updated list
show_magicians(magician_names)