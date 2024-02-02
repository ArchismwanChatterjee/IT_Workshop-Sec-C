try:
    # Read a number from the user
    number = float(input("Enter a number: "))
    
    # Calculate and print the square
    square = number ** 2
    print(f"The square of {number} is: {square}")

except ValueError as ve:
    print(f"Error: {ve}")
except KeyboardInterrupt:
    print("\nCtrl + C pressed. Program terminated.")
