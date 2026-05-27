# Get input from the user
user_input = input("Enter a number: ")

try:
    num = int(user_input)

    if num > 0:
        print(f"{num} is a natural number!")
    else:
        print(f"{num} is NOT a natural number.")
except ValueError:
    print("Invalid input! Please enter a whole number.")

