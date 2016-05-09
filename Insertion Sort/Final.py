import random

# creating array of random ints
numbers = [int(random.random() * 20) for _ in range(100)]

# printing array so we know what were looking at
print(numbers)

# insertion sort
def insertionSort(numbers):
    for index in range(1, len(numbers)):
        currentValue = numbers[index]
        position = index

        while position > 0 and numbers[position - 1] > currentValue:
            numbers[position] = numbers[position - 1]
            position -= 1

        numbers[position] = currentValue

# test and print out the result
insertionSort(numbers)
print(numbers)