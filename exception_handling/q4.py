import random

class InfiniteRandomNumbers:
    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < 10:
            self.count += 1
            return random.randint(1, 100)  # Adjust the range as needed
        else:
            raise StopIteration

# Create an instance of InfiniteRandomNumbers
infinite_numbers = InfiniteRandomNumbers()

# Iterate through the random numbers
for number in infinite_numbers:
    print(number)

