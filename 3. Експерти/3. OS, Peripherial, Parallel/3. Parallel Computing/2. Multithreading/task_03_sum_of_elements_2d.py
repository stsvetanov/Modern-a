import math
import multiprocessing
import threading
from random import randint

data = [[j for j in range(4)] for k in range(4)]
partial_sum = [0, 0, 0, 0]
print(data)

number_of_cpus = multiprocessing.cpu_count()


def task1():
    name = threading.current_thread().name
    # print(f"Hello from thread {name}")

    thread_index = int(name)
    size = len(data)
    for i in range(thread_index, size, number_of_cpus):
        partial_sum[thread_index] = partial_sum[thread_index] + sum(data[i])



if __name__ == "__main__":

    for i in range(number_of_cpus):
        thread_name = f'{i}'
        thread_name = threading.Thread(target=task1, name=thread_name)
        thread_name.start()

    print(sum(partial_sum))
