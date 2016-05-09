import random

# creating array of random ints
numbers = [int(random.random() * 20) for _ in range(100)]

# printing array so we know what were looking at
print(numbers)

# Simple search
def simpleSearch(numbers, goal):
    # Your code here

def indexesSearch(numbers, goal):
    # Your code here

# test the functions

print(simpleSearch(numbers, 7))
print(indexesSearch(numbers, 7))