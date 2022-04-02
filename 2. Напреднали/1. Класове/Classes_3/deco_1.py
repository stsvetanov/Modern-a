def decorator(F):
    def wrapper(*args):
        print(" Преди извикване на функцията ")
        F(*args)
        print(" След извикване на функцията ")
    return wrapper

@decorator
def func():
    print ("Hello")

func()

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls,self.func.__name__))
        return self.func(*args)

@tracer
def spam(a, b, c):
    print(a + b + c)
spam(1,2,3)
spam(3,4,5)