import multiprocessing
import threading
import timeit

# number_of_cpus = multiprocessing.cpu_count()
number_of_cpus = 1
print(f"Number of threads: {number_of_cpus}")
barrier = threading.Barrier(number_of_cpus + 1)

is_prime = True


def is_prime_number(number):
    global is_prime
    name = threading.current_thread().name

    thread_index = int(name)
    if number > 1:
        for i in range(thread_index, int(number/2), number_of_cpus):
            if (number % i) == 0:
                is_prime = False
                break
    barrier.wait()


if __name__ == "__main__":
    number = int(input("Enter any number: "))

    starttime = timeit.default_timer()
    for i in range(2, number_of_cpus + 2):
        thread_name = f'{i}'
        thread_name = threading.Thread(target=is_prime_number, name=thread_name, args=(number,))
        thread_name.start()

    barrier.wait()
    print("The time difference is :", timeit.default_timer() - starttime)
    print(is_prime)