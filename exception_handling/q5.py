class BelowThresholdError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Error: {value} is below the threshold (0.5)")

def generate_random_number():
    number = random.random()  # Generates a random float between 0 and 1
    print("Generated random number:", number)
    
    if number < 0.5:
        raise BelowThresholdError(number)

# Import the random module
import random

try:
    generate_random_number()

except BelowThresholdError as bte:
    print(bte)
