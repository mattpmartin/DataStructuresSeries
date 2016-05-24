import random

# creating array of random ints
numbers = [int(random.random() * 20) for _ in range(100)]

# printing array so we know what were looking at
print(numbers)

# Shell sort
def mergeSort(numbers):
    if len(numbers) > 0:
        mid = len(numbers) // 2

        leftHalf = numbers[:mid]
        rightHalf = numbers[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        x = 0
        y = 0
        z = 0

        while x < len(leftHalf) and y < len(rightHalf):
            if leftHalf[x] < rightHalf[y]:
                numbers[z] = leftHalf[x]
                x += 1

            else:
                numbers[z] = rightHalf[y]
                y += 1

            k += 1

        while x < len(leftHalf):
            numbers[z] = leftHalf[x]
            x += 1
            z += 1

        while y < len(rightHalf):
            numbers[z] = rightHalf[y]
            y += 1
            z += 1

# test the functions

print(mergeSort(numbers))