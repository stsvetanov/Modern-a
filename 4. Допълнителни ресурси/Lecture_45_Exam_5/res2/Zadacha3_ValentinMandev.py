import threading as mp

is_prime = True


def is_number_prime(start, end):
    global is_prime
    for numbers in range(2, number):
        if number % numbers == 0:
            is_prime = False
    return is_prime


number = int(input())
number_of_threads = 2

if __name__ == '__main__':
    partition_size = number / number_of_threads
    for i in range(0, number, partition_size):
    p = mp.Thread(target = is_number_prime, args = (start, end,))
    p.start()
    print(is_prime)
    p.join()


