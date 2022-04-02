def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def compute(func, a, b):
    return func(a, b)


print(add(5, 7))

print(compute(mul, 5, 5))
print(compute(add, 5, 5))

