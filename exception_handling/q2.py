def perform_operations(num1, num2):
    try:
        addition_result = num1 + num2
        print(f"Addition: {num1} + {num2} = {addition_result}")

        subtraction_result = num1 - num2
        print(f"Subtraction: {num1} - {num2} = {subtraction_result}")

        multiplication_result = num1 * num2
        print(f"Multiplication: {num1} * {num2} = {multiplication_result}")

        if num2 != 0:
            division_result = num1 / num2
            print(f"Division: {num1} / {num2} = {division_result}")
        else:
            raise ZeroDivisionError("Error: Division by zero is not allowed.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    perform_operations(num1, num2)

except ValueError as ve:
    print(f"Error: {ve}")

'''
Enter the first number: 4
Enter the second number: 5
Addition: 4.0 + 5.0 = 9.0
Subtraction: 4.0 - 5.0 = -1.0
Multiplication: 4.0 * 5.0 = 20.0
Division: 4.0 / 5.0 = 0.8
'''