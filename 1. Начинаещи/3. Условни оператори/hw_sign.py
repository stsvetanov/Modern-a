# Решение 1
# x = -3
# y = -4
# z = -5
#
# if x * y * z < 0 == True:
#     print("Minus Sign")
# else:
#     print("Plus Sign")

# Решение 2
# n = int(input("Въведете броят на умножаваните числа: "))
# sum_negative = 0
#
# for i in range(n):
#     num_i = int(input(f"Въведете число {i + 1}: "))
#     if num_i < 0:
#         sum_negative += 1 # Броят на числата в произведението, които са по-малки от нула.
# if sum_negative % 2 == 0:
#     print("Резултатът от произведението на числата е положителен.")
# else:
#     print("Резултатът от произведението на числата е отрицателен.")

# Решение 3
# i = 0
# sum_negative = 0
# while True:
#     num_i = input()
#     if num_i != "" and int(num_i) < 0:
#         sum_negative += 1 # Броят на числата в произведението, които са по-малки от нула.
#     elif num_i == "":
#         break
#     i += 1
# if i == 1:
#     print("Произведението е между най-малко две числа")
# elif i > 1 and sum_negative % 2 == 0:
#     print("Резултатът от произведението на числата е положителен.")
# else:
#     print("Резултатът от произведението на числата е отрицателен.")

# Решение 4
txt = '2*-4*5*-6*-4'
ctr = 0
for i in txt:
    if i == '-':
        ctr += 1

if ctr % 2 == 0:
    print('+')
else:
    print('-')

