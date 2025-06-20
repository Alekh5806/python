try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except ZeroDivisionError:
    print("❗ Cannot divide by zero.")
except ValueError:
    print("❗ Please enter only numbers.")