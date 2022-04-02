#Използвам 3 нишки за решаване на задачата

import math
import threading

number = int(input("Въведете число: "))
max_divisor = math.floor(math.sqrt(number))
has_divisor = False
number_of_threads = 3


def check_divisor(divisible, divisor):
    global has_divisor
    check_res = (divisible % divisor == 0)
    has_divisor = has_divisor | check_res


def is_prime(number):
    name = threading.current_thread().name
    thread_index = int(name)
    for i in range(thread_index, 1 + max_divisor, number_of_threads):
        check_divisor(number, i)


def multitasking():
    for d in range(2, number_of_threads + 2):
        thread_name = f'{d}'
        thread_name = threading.Thread(target=is_prime, args=(number,), name=thread_name)
        thread_name.start()


if number == 1:
    print(False)
else:
    multitasking()
    if has_divisor == False:
        print(True)
    else:
        print(False)