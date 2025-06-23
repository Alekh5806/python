print("Enter your name for the guest book. (Type 'q' to quit)")

while True:
    name = input("Name: ")
    if name.lower() == 'q':
        break
    print(f"Hello {name.title()}, you’re added to the guest book!")

    with open("guest_book.txt", "a") as file:
        file.write(f"{name.title()}\n")