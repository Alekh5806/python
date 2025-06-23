# Function with default values
def make_shirt(size='Large', message='I love Python'):
    print(f"Making a shirt of size {size} with the message: '{message}'")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size='Medium')

# Custom shirt with your own message
make_shirt('Small', 'Keep Calm and Code On')