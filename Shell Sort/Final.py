import random

# creating array of random ints
numbers = [int(random.random() * 20) for _ in range(100)]

# printing array so we know what were looking at
print(numbers)

# Shell sort
def shellSort(numbers):
    increment = len(numbers) // 2

    while increment >0:

        for start in range(increment):
            shellInsertionSort(numbers, start, increment)

        increment = increment // 2

# sort for each shell
def shellInsertionSort(numbers, start, i):
    for index in range(start + i, len(numbers), i):
        currentValue = numbers[index]
        position = index

        while position >= i and numbers[position - i] > currentValue:
            numbers[position] = numbers[position - i]
            position -= i

        numbers[position] = currentValue

# test the functions

print(shellSort(numbers))