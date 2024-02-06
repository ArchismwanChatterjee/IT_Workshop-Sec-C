try:
    number = float(input("Enter a number: "))
    square = number ** 2
    print(f"The square of {number} is: {square}")

except ValueError as ve:
    print(f"Error: {ve}")
except KeyboardInterrupt:
    print("\nCtrl + C pressed. Program terminated.")

'''
Enter a number: 5
The square of 5.0 is: 25.0
'''