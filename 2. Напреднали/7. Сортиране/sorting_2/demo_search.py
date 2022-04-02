# my_list = [4, 5, 23, 564, 23, 12, 54, 23, 23, 11, 34]
#
# object_to_search = 23
# index = my_list.index(object_to_search)
# if my_list.index(object_to_search) is None:
#     print(f'Object not found')
# else:
#     print(f"Object {object_to_search} at position {index}")


# my_string = "asdfasdfklajsdlkfjad;slkjf adsk"
# print(my_string.find("f"))


def my_find_function(target, my_string):
    l = len(target)
    for index, item in enumerate(my_string):
        if my_string[index: index + l] == target:
            return index
    return -1

my_string = "asdfasdfklajsdlkfjad;slkjf adsk"
target = "adskds"

print(my_find_function(target, my_string))



# Search in ordered list
# "123456789"