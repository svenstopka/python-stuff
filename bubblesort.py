from numpy import random
array = random.randint(100, size=10)
print(array)
for i in range(len(array)):
    swap = False
    for j in range(len(array) - 1):
        if array[j + 1] < array[j]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp
            swap = True
    if not swap:
        break
print(array)
