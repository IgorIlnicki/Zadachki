import random

def get_n(min, max, quantity):
    lottery_numbers = set()
    for i in range(quantity):
        lottery_numbers.add(random.randint(min, max))
    return sorted(lottery_numbers)

result = get_n(1,49,21)
print(result)