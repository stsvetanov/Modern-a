# my_string = 'aasdfdsasdf'
# my_string1 = "asdfasdfa fa"
#
# my_tuple = ("asdf", 212, 2.3, "Hi")
#
# my_string = my_string.replace('s', 'S')
# my_string.join("he he !")
#
# print(my_string[1:6])
# print(my_tuple[2])
#
#
#
# my_list = ["asdf", "wew", 23, 33, 323.3]
# my_list.append("50")
# my_list.pop(2)
#
#
# my_set = {32, 43, 45, 23, 23, 32, 'j', 'i', 't', 'a', 'o', 'l', 'p', 'e', 'g', 'k', ';'}
# my_set.add(15)
# print(my_set)
#
# my_set2 = set("a;sdlkjf;alksdjf;akdsjf;akljdsfpoiwuerpiojkghlskjdfghjlsfdghsdfghpioudfgpiosjdpfjdghpaoshtgpoiwqehtpoiahfgpoiaudfjpoaisdfipoasdjfpoiahdga")
# print(my_set2)
# my_set2.intersection(my_set)
#
my_dict = {'Sofia': 12, 'Кола': 'Car'}
#
# value = my_dict.get("Кола")
# print(value)
# my_dict['Paris'] = 10
# print(my_dict)
# my_dict['Paris'] = 90
# print(my_dict)
# my_dict[my_string] = 34
# my_dict[my_tuple] = 8098049830
# # my_dict[my_list] = "9asdf" # Error: unhashable type: 'list' (List is mutable)
#
# # Iterables
# # for element in my_string1:
# #     print(element)
#
# # for element in enumerate(my_string1):
# #     print(element) # tuple
# #
# # for index, element in enumerate(my_string1):
# #     print(index)
# #     print(element)
#
# # for element in my_set:
# #     print(element)
#
print("*****************")
print(my_dict)

for element in my_dict.items():
    print(element)

for key, value in my_dict.items():
    print("{}: {}".format(key, value))
#
#
#
#

