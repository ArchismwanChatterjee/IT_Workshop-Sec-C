try:
    # Read a number from the user
    number = float(input("Enter a number: "))
    
    # Check if the number is positive or zero
    if number >= 0:
        print("The entered number is:", number)
    else:
        # Raise an exception for negative numbers
        raise ValueError("Error: Entered number is negative")

except ValueError as e:
    print(e)
