class BelowThresholdError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Error: {value} is below the threshold (0.5)")

def generate_random_number():
    number = random.random() 
    print("Generated random number:", number)
    
    if number < 0.5:
        raise BelowThresholdError(number)

import random

try:
    generate_random_number()

except BelowThresholdError as bte:
    print(bte)

'''
Generated random number: 0.5552496065285105
'''