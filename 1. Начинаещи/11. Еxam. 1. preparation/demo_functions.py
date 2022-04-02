def my_sum_func(a, b):
    return a + b


# result = my_sum_func(5, 6)
# print(result)


def calc_factorial(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial = factorial * i
    return factorial

# 5! = 5*4! = 5*4*3! = ...= 5*4*3*2*1

def calc_factorial_rec(n):
    if n == 1:
        return 1
    factorial = n * calc_factorial_rec(n - 1)
    return factorial


factorial = calc_factorial(5)
print(factorial)

factorial = calc_factorial_rec(5)
print(factorial)


