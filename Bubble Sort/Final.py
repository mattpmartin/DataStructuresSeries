import random

# creating array of random ints
numbers = [int(random.random() * 20) for _ in range(100)]

# printing array so we know what were looking at
print(numbers)

# bubble sort
def bubbleSort(numbers):
    # simple bubble sort
    # for passnum in range(len(numbers) - 1, 0, -1):
    #     for i in range(passnum):
    #         if numbers[i] > numbers[i + 1]:
    #             numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    #

    # short bubble
    for passnum in range(len(numbers) - 1, 0, -1):
        ordered = True
        for i in range(passnum):
                if numbers[i] > numbers[i + 1]:
                    ordered = False
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

        if ordered:
            break

# test and print out the result
bubbleSort(numbers)
print(numbers)