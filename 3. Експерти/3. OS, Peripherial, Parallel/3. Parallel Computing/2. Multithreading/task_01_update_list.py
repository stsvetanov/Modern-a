import math
import multiprocessing
import threading
from random import randint

data = [randint(1, 20) for _ in range(20)]
print(data)

number_of_cpus = multiprocessing.cpu_count()


def task1():
    name = threading.current_thread().name
    # print(f"Hello from thread {name}")

    thread_index = int(name)
    size = len(data)
    for i in range(thread_index, size, number_of_cpus):
        data[i] = data[i] + 1



if __name__ == "__main__":

    for i in range(number_of_cpus):
        thread_name = f'{i}'
        thread_name = threading.Thread(target=task1, name=thread_name)
        thread_name.start()

    print(data)
