# # If mark > 3.5 -> pass
# x = 100
#
# if x >= 3.5:
#     print("Pass")
# else:
#     print("Fail")

x = float(input("Въведете оценка: "))
# x = float(x)

if x < 3:
    print("Слаб")
elif x < 3.5:
    print('Среден')
elif x < 4.5:
    print('Добър')
elif x < 5.5:
    print("Мн.Добър")
elif x <= 6:
    print("Отличен")
else:
    print("Оценката е извън скалата")
