while True:
    topping = input("Enter a pizza topping (or type 'quit' to stop): ")

    if topping.lower() == 'quit':
        print("Finished taking your order. Enjoy your pizza!")
        break
    else:
        print(f"Adding {topping} to your pizza.")