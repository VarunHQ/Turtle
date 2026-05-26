number = int(input("Enter a number to check if it is even or odd: "))
print(f"The number to be checked is: {number}")

if number % 2 == 0:
    print(f"{number} is an even number.")

else:
    print(f"{number} is an odd number.")