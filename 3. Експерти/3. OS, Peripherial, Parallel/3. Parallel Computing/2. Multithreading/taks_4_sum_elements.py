import threading
from random import randint
from multiprocessing import cpu_count
barrier = threading.Barrier(4)

my_data = [[1 for _ in range(10000)] for _ in range(10000)]
# print(my_data)
partial_sum = [0 for _ in range(cpu_count())]
# print(partial_sum)


def find_partial_sum():
    name = threading.current_thread().name
    print(name)
    thread_index = int(name)
    for k in range(thread_index, len(my_data), cpu_count()):
        partial_sum[thread_index] += sum(my_data[k])
    # barrier.wait()


print(f"Total sum: {sum(partial_sum)}")
my_sum = 0
for item in my_data:
    my_sum += sum(item)

print(my_sum)