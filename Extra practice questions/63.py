topping = ""
while topping.lower() != 'quit':
    topping = input("Enter a topping (or 'quit' to exit): ")
    if topping.lower() != 'quit':
        print(f"Adding {topping} to your pizza.")


while True:
    topping = input("Enter a topping (or 'quit' to exit): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza.")


active = True
while active:
    topping = input("Enter a topping (or 'quit' to exit): ")
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")