import random

# creating array of random ints
numbers = [int(random.random() * 20) for _ in range(100)]

# printing array so we know what were looking at
print(numbers)

# Shell sort
def shellSort(numbers):
    # Your code here

# sort for each shell
def shellInsertionSort(numbers, start, i):
    # Your code here

# test the functions

print(shellSort(numbers))