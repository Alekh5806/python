while True:
    age_input = input("Enter your age (or type 'quit' to exit): ")

    if age_input.lower() == 'quit':
        print("Thanks for checking ticket prices!")
        break

    age = int(age_input)

    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")