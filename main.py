import string
from functions import Caluclator_Functions as f

while True:
    try:
        user_choice = int(input("What calculation would you like to do? (1. Add, 2. Subtract, 3. Multiply, 4. Divide)?: "))
        while user_choice not in [1,2,3,4]:
            user_choice = int(input("Please enter a valid choice. (1. Add, 2. Subtract, 3. Multiply, 4. Divide)?: "))
        else:
            break
    except ValueError:
        print("Please")


while True:
        try:
            value1 = float(input("What is X equal to?: "))
            break
        except ValueError:
            print("Please enter a valid number")

while True:
        try:
            value2 = float(input("What is Y equal to?: "))
            break
        except ValueError:
            print("Please enter a valid number")

