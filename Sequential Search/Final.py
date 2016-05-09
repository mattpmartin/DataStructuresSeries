import random

# creating array of random ints
numbers = [int(random.random() * 20) for _ in range(100)]

# printing array so we know what were looking at
print(numbers)

# Simple search
def simpleSearch(numbers, goal):
    for number in numbers:
        if number == goal:
            return True

    return False

def indexesSearch(numbers, goal):
    indexes = []

    for index, number in enumerate(numbers):
        if number == goal:
            indexes.append(index)

    return indexes

# test the functions

print(simpleSearch(numbers, 7))
print(indexesSearch(numbers, 7))