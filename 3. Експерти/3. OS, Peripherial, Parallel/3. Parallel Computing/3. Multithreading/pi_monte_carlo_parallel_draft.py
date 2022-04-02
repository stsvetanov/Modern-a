import multiprocessing
from random import *

MAXN = 10000000


def calculate_monte_carlo_part(n):
    hits = 0

    for _ in range(1, n + 1):
        x = random()
        y = random()
        if x * x + y * y <= 1.0:
            hits += 1

    return hits


if __name__ == '__main__':
    np = multiprocessing.cpu_count()
    partitions = [int(MAXN/np)] * np
    print(partitions)

    pool = multiprocessing.Pool(processes=np)
    counts = pool.map(calculate_monte_carlo_part, partitions)

    hits = sum(counts)

    print(hits, '* 4.0 /', MAXN, '=', hits * 4.0 / MAXN)
