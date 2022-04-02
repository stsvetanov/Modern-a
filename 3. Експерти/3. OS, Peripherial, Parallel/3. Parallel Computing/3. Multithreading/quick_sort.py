import random


def quick_soft(array):
    if len(array) <= 1:
        return array

    pivot = array[int(len(array)/2)]
    mid = [x for x in array if x == pivot]
    left = [x for x in array if x < pivot]
    right = [x for x in array if x > pivot]
    return quick_soft(left) + mid + quick_soft(right)


my_list = [random.randint(1, 20) for _ in range(50)]
print(quick_soft(my_list))

