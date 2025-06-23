print("Let's add two numbers! (Type 'q' to quit)\n")

while True:
    num1 = input("Enter first number: ")
    if num1.lower() == 'q':
        break
    num2 = input("Enter second number: ")
    if num2.lower() == 'q':
        break

    try:
        sum_result = int(num1) + int(num2)
    except ValueError:
        print("❌ That wasn't a number. Please enter **valid integers only**.\n")
    else:
        print(f"✅ The result is: {sum_result}\n")