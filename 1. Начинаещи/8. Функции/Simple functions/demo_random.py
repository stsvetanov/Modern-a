'''
Mutable list
'''
import random

def remove_element(list):
    list.pop(random.randint(0, len(list)-1))
    return list


my_list = [i for i in range(10)]
print(my_list)
new_list = remove_element(my_list)
print(new_list)
print(my_list)

