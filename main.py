import string

while True:
    try:
        user_input = float(input("What calculation would you like to do? (1. Add, 2. Subtract, 3. Multiply, 4. Divide)?: "))
        break

    except ValueError:
        print("Invalid input")