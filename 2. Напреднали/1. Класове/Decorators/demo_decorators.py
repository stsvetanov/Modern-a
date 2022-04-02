from functools import wraps


def my_decorator(function):
    @wraps(function)
    def wrapper(a, b, c):
        print("I'm in decorator")
        a += 1
        b += 1
        c += 1
        return function(a, b, c)
    return wrapper


@my_decorator
def my_print(a, b, c):
    print("I'm in function")
    print(f'{a}, {b}, {c}')


# my_print = my_decorator(my_print)
my_print(1, 2, 3)
