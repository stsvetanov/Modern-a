# Задача: Колко числа от матрицата попадат в даден интервал?


# Необходими модули
import numpy as np
from time import time

# Дефиниране на функциите за решаване на задачата за даден ред

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

def howmany_within_range_asinch(i, row, minimum, maximum):
    # Решава се същата задача, но има един допълнителен парамаетър i,
    # който всъщност идва от цикъла за асинхронното паралелизиране
    # Използваемост: само при асинхронна паралелилзация за pool.apply() и pool.starmap()
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return (i, count)

# Генериране на данните
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
data[:5]

# Решение без паралелизация
# =========================
results = []
for row in data:
    results.append(howmany_within_range_sinch(row, minimum=4, maximum=8))

print(results[:10])
#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]

# Паралелно Синхронно изпълнение чрез apply(), map() и starmap()
#================================================================

import multiprocessing as mp
# Step 1: Init multiprocessing.Pool()
pool = mp.Pool(mp.cpu_count())

# Step 2: Sinchoronous Parallel Processing the `howmany_within_range()`
results_sinch_apply = [pool.apply(howmany_within_range_sinch, args=(row, 4, 8)) for row in data]
results_sinch_map = pool.map(howmany_within_range_sinch, [row for row in data])
results_sinch_starmap = pool.starmap(howmany_within_range_sinch, [(row, 4, 8) for row in data])

# Step 3: Don't forget to close
pool.close()
print(results_sinch_apply[:10])     #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
print(results_sinch_map[:10])       #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
print(results_sinch_starmap[:10])   #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]

# Паралелно Асинхронно изпълнение чрез apply(), map() и starmap()
#================================================================

# Паралелизация с Pool.apply_async() и callback
#---------------------------------------------------------
pool = mp.Pool(mp.cpu_count())
results_asinc_apply = []
# Step 1: Define callback function to collect the output in `results`
def collect_result(result):
    global results_asinc_apply
    results.append(result)
# Step 2: Use loop to parallelize
for i, row in enumerate(data):
    pool.apply_async(howmany_within_range_asinch, args=(i, row, 4, 8), callback=collect_result)
# Step 3: Close Pool and let all the processes complete
pool.close()
pool.join()  # отлага изпълнението на следващата линия от кода докато всички процеси в опашката не приключат работа

# Step 4: Sort results [по избор]
results_asinc_apply.sort(key=lambda x: x[0])
results_asinc_apply_final = [r for i, r in results_asinc_apply]

print(results_asinc_apply_final[:10])  #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]

# Паралелизация с Pool.starmap_async() и Pool.map_async()
#---------------------------------------------------------------
pool = mp.Pool(mp.cpu_count())
results_asinc_starmap = []
results_asinc_map=[]
results_asinc_starmap = pool.starmap_async(howmany_within_range_asinch, [(i, row, 4, 8) for i, row in enumerate(data)]).get()
results_asinc_map = pool.map_async(howmany_within_range_sinch, [row for row in data]).get()
pool.close()
print(results_asinc_starmap[:10]) #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
print(results_asinc_map[:10]) #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]