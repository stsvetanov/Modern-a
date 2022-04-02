import random

my_list = [random.randint(0, 100) for _ in range(10)]
print('Разбъркани', my_list)


def SelectionSort(my_list):
    for i in range(len(my_list)):
        min_idx = i
        for j in range(i + 1, len(my_list)):
            if my_list[min_idx] > my_list[j]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]

SelectionSort(my_list)
print('Подредени',my_list)