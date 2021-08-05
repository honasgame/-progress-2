import random

def generator():
    
    for i in range(6):
        yield random.randint(1, 10)

    
    yield random.randint(1,5)

for random_number in generator():
       print( (random_number))