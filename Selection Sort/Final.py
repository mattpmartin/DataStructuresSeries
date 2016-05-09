import random

# creating array of random ints
numbers = [int(random.random() * 20) for _ in range(100)]

# printing array so we know what were looking at
print(numbers)

# selection sort
def selectionSort(numbers):
    for fillspot in range(len(numbers) -1, 0, -1):
        maxPosition = 0

        for i in range(1, fillspot + 1):
            if numbers[i] > maxPosition:
                maxPosition = i

        numbers[fillspot], numbers[maxPosition] = numbers[maxPosition], numbers[fillspot]

# test and print out the result
selectionSort(numbers)
print(numbers)