'''
5
-3
2
(-)

2
-8
-2
(+)
Ако отрицателните числа са нечетен брой, то произведениеото е отрицателно.
Може да се използва променлия в която да се записва броя на отрицателните числа. negative_numbers_count
'''

numbers = [1, 4, -4, 23, 12, -23, 434, 3, 23, -3, -34]

negative_numbers_count = 0

for number in numbers:
    if number < 0:
        # negative_numbers_count = negative_numbers_count + 1
        negative_numbers_count += 1


if negative_numbers_count % 2 == 0:
    print('Произведението е положително')
else:
    print('Произведението е отрицателно')





