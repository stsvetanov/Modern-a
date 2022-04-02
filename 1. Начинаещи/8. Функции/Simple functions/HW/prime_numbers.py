# Проверява дали въведеното число е просто
def is_prime(arg):
    dlt = arg - 1
    ctr = 0
    while dlt > 1:
        if arg % dlt == 0:
            ctr += 1
        dlt -= 1
    if ctr < 1:
        print(f'{arg} is Prime')
    else:
        print(f'{arg} is not Prime')


n = int(input('Въведете число: '))
is_prime(n)

# Извежда редица от прости числа в диапазон
def prime_numbers(arg):
    for num in range(1,arg):
        ctr = 0
        for dlt in range(num - 1, 1, -1):
            if num % dlt == 0:
                ctr += 1
        if ctr < 1:
            print(num)

prime_numbers(n)