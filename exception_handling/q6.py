class NegativeAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Error: Age cannot be negative ({age})")

def get_person_age():
    age = int(input("Enter the age of the person: "))
    
    if age < 0:
        raise NegativeAgeError(age)
    
    print(f"The entered age is: {age}")

try:
    get_person_age()

except NegativeAgeError as nae:
    print(nae)
except ValueError:
    print("Error: Please enter a valid integer for age.")
