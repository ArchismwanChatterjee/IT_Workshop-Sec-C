def perform_operations(num1, num2):
    try:
        # Addition
        addition_result = num1 + num2
        print(f"Addition: {num1} + {num2} = {addition_result}")

        # Subtraction
        subtraction_result = num1 - num2
        print(f"Subtraction: {num1} - {num2} = {subtraction_result}")

        # Multiplication
        multiplication_result = num1 * num2
        print(f"Multiplication: {num1} * {num2} = {multiplication_result}")

        # Division
        if num2 != 0:
            division_result = num1 / num2
            print(f"Division: {num1} / {num2} = {division_result}")
        else:
            raise ZeroDivisionError("Error: Division by zero is not allowed.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")

# Get input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform mathematical operations
    perform_operations(num1, num2)

except ValueError as ve:
    print(f"Error: {ve}")
