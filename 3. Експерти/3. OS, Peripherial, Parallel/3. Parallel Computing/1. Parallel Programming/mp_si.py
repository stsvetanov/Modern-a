import numpy as np
import time as t
def howmany_within_range_sinch(row, minimum=4, maximum=8):
    # Функцията се използва и в решението без паралелизация
    # Задаването на стойности по подразбиране за minimum и maximum на интервала е необходимо, за да може с функцията
    # да се работи и чрез pool.map()
    # Връща колко числа попадат в посочения интервал в даден конкретен ред
    # Използваемост: без паралелизация, синхроннна паралелизация, pool.map_async()

    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count
# Генериране на данните
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
import multiprocessing as mp
#mp.set_start_method('fork')
t_1=t.time()
# Step 1: Init multiprocessing.Pool()
pool = mp.Pool(mp.cpu_count())

# Step 2: Sinchoronous Parallel Processing the `howmany_within_range()`
results_sinch_apply = [pool.apply(howmany_within_range_sinch, args=(row, 4, 8)) for row in data]
#results_sinch_map = pool.map(howmany_within_range_sinch, [row for row in data])
#results_sinch_starmap = pool.starmap(howmany_within_range_sinch, [(row, 4, 8) for row in data])

# Step 3: Don't forget to close
pool.close()
t_2=t.time()
dt_norm=t_2-t_1