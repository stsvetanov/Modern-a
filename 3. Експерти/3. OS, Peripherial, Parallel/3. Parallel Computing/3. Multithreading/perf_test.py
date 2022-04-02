import math
import timeit

starttime = timeit.default_timer()
for i in range(1000000):
    a = math.atan(i)
print("The time difference is :", timeit.default_timer() - starttime)