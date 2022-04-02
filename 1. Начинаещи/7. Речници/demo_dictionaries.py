# my_dict = dict()  # създава нов празен речник
#
# my_dict = {}  # идентично с горното. Това е приетият начин в света на Python да се създават нови речници
#
# len(my_dict)  # връща броя на елементите (ключовете) в речника
#
# del my_dict['key']  # премахва ключа и неговата стойност от речника
#
# 'my_key' in my_dict  # връща True ако 'my_key' съществува в речника, независимо от стойността, False ако го няма
#
# 'my_key' not in my_dict  # връща False ако 'my_key' съществува в речника, независимо от стойността, True ако го няма
#
# my_dict.clear(my_dict)  # премахва всички ключове и стойности от речника
#
# my_dict.get('my_key')  # връща стойността за 'my_key'. Ако 'my_key' не съществува се връща None

weather = {
    'София': 30,
    'Новосибирск': -31,
    'Таити': 30
}

# print(weather.get('София'))
#
# keys = weather.keys()
# print(type(keys))
# print(weather.keys())

# for key in weather:
#     print(key)  # при всяка итерация променливата key ще бъде един от ключовете в речника
#     print(weather[key])  # тъй като имаме ключа може да вземем и стойността асоциирана с него
#
for key, value in weather.items():
    print(key)
    print(value)

for value in weather.items():
    print(value)