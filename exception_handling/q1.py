try:
    number = float(input("Enter a number: "))
    
    if number >= 0:
        print("The entered number is:", number)
    else:
        raise ValueError("Error: Entered number is negative")

except ValueError as e:
    print(e)
'''
Enter a number: 56
The entered number is: 56.0
'''