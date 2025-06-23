# Function to describe a sandwich
def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f" - {item}")

# Function calls
make_sandwich('cheese', 'tomato')
make_sandwich('lettuce', 'onion', 'mayonnaise', 'chicken')
make_sandwich('paneer', 'capsicum', 'chilli flakes')