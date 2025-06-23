print("Give me two numbers and I’ll add them. Type 'q' to quit.\n")

while True:
    num1 = input("First number: ")
    if num1.lower() == 'q':
        break
    num2 = input("Second number: ")
    if num2.lower() == 'q':
        break

    try:
        result = int(num1) + int(num2)
    except ValueError:
        print("Oops! Please enter **numbers only**, not text.\n")
    else:
        print(f"The sum is: {result}\n")