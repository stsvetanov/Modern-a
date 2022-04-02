def check_if_prime(number):
    is_prime = True
    for i in range(2, int(number/2)):
        if number % i == 0:
            is_prime = False
            break

    return is_prime

print(check_if_prime(101))