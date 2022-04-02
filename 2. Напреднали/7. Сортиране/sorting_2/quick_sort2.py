import random

def sort(array):
    if len(array) <= 1:
        return array
    pivot = array[int(len(array) / 2)]
    left = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return sort(left) + equal + sort(right)


array = [random.randint(0, 100000) for _ in range(50000)]
# array = [12, 4, 5, 6, 7, 3, 1, 15]
print(array)
print(sort(array))
