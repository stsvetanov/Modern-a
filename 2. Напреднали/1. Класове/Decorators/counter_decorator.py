COUNTER = 0


def counter(function):
    def wrapper(*args, **kwargs):
        global COUNTER
        COUNTER += 1
        print(COUNTER)
        return function(*args, **kwargs)
    return wrapper


@counter
def my_func(test_to_print):
    print(test_to_print)


my_func("Hi")
my_func("Hi")
my_func("Hi")

