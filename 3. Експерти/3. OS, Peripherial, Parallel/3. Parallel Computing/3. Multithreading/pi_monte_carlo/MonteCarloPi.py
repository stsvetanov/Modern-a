from random import *

MAXN = 10000000


def dist(x, y):
    return x * x + y * y


hits = 0

for _ in range(1, MAXN + 1):
    x = random()
    y = random()
    if dist(x, y) <= 1.0:
        hits += 1

print(hits, '* 4.0 /', MAXN, '=', hits * 4.0 / MAXN)
