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

a = -2
b = 5
c = 12
t = 23

negative_numbers_count = 0

if a < 0:
    # negative_numbers_count = negative_numbers_count + 1
    negative_numbers_count += 1
if b < 0:
    negative_numbers_count += 1
if c < 0:
    negative_numbers_count += 1

if negative_numbers_count % 2 == 0:
    print('Произведението е положително')
else:
    print('Произведението е отрицателно')





