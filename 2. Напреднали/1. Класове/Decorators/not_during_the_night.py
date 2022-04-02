# https://realpython.com/primer-on-python-decorators
from datetime import datetime


def not_during_the_night(function):
    def wrapper():
        if 7 < datetime.now().hour < 22:
            function()
        else:
            print("Neighbors are sleeping")
    return wrapper


@not_during_the_night
def say_hi():
    print("Hi")


# say_hi = not_during_the_night(say_hi)

say_hi()
