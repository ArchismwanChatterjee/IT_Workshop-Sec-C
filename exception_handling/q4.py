import random

class InfiniteRandomNumbers:
    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < 10:
            self.count += 1
            return random.randint(1, 100)  
        else:
            raise StopIteration

infinite_numbers = InfiniteRandomNumbers()

for number in infinite_numbers:
    print(number)

'''
71
44
14
57
33
58
92
91
43
66
'''
